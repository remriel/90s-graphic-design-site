"""NOIZ: original 10-second 90s earbuds concept campaign.
Run: python render.py --output /path/to/deliverables [--preview]
Dependencies: Pillow, numpy, imageio-ffmpeg. Fonts default to Windows system fonts.
"""
from pathlib import Path
from functools import lru_cache
import argparse, math, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

ROOT=Path(__file__).resolve().parent
W,H,FPS=1080,1920,30
C={'ink':'#080808','paper':'#fffdf1','pink':'#ff2ba6','aqua':'#00e7dc','yellow':'#fff200','purple':'#6236ff'}
FONT=Path('C:/Windows/Fonts')
@lru_cache(None)
def fnt(size,mono=False): return ImageFont.truetype(str(FONT/('courbd.ttf' if mono else 'impact.ttf')),size)
@lru_cache(180)
def label(s,size,color='paper',stroke=0,mono=False):
 f=fnt(size,mono); b=f.getbbox(s,stroke_width=stroke); im=Image.new('RGBA',(b[2]-b[0]+8,b[3]-b[1]+8)); ImageDraw.Draw(im).text((4-b[0],4-b[1]),s,font=f,fill=C.get(color,color),stroke_width=stroke,stroke_fill=C['ink']); return im
def put(im,s,x,y,size,color='paper',stroke=0,mono=False,shadow=False):
 if shadow: im.alpha_composite(label(s,size,'ink',stroke,mono),(int(x+12),int(y+14)))
 im.alpha_composite(label(s,size,color,stroke,mono),(int(x),int(y)))
def fit(im,s,x,y,width,size,color='paper',stroke=0,shadow=False):
 a=label(s,size,color,stroke); a=a.resize((width,a.height),Image.Resampling.LANCZOS)
 if shadow:
  sh=Image.new('RGBA',a.size,C['ink']);sh.putalpha(a.getchannel('A'));im.alpha_composite(sh,(int(x+12),int(y+14)))
 im.alpha_composite(a,(int(x),int(y)))
def ease(u): return 1-(1-max(0,min(1,u)))**4
def chip(im,s,x,y,bg='pink',fg='paper',angle=-4,size=42):
 a=label(s,size,fg,0,True); card=Image.new('RGBA',(a.width+48,a.height+32),C[bg]); ImageDraw.Draw(card).rectangle((0,0,card.width-1,card.height-1),outline=C['ink'],width=5); card.alpha_composite(a,(24,16));card=card.rotate(angle,expand=True,resample=Image.Resampling.BICUBIC); sh=Image.new('RGBA',card.size,C['ink']);sh.putalpha(card.getchannel('A'));im.alpha_composite(sh,(int(x+9),int(y+12)));im.alpha_composite(card,(int(x),int(y)))

product=Image.open(ROOT/'assets/earbuds.png').convert('RGBA');product=product.crop(product.getbbox())
def prod(im,cx,cy,height,angle=0):
 a=product.resize((int(product.width*height/product.height),int(height)),Image.Resampling.LANCZOS).rotate(angle,expand=True,resample=Image.Resampling.BICUBIC)
 sh=Image.new('RGBA',a.size,C['ink']);sh.putalpha(a.getchannel('A').point(lambda p:int(p*.35)))
 x=int(cx-a.width/2);y=int(cy-a.height/2);im.alpha_composite(sh,(x+24,y+30));im.alpha_composite(a,(x,y))

def ticker(im,t,y=1680,bg='ink',fg='aqua'):
 d=ImageDraw.Draw(im);d.rectangle((0,y,W,y+85),fill=C[bg]);s='NOIZ / WIRELESS EARBUDS / ';a=label(s,38,fg,0,True);off=int(t*140)%a.width
 for x in range(-off,W,a.width):im.alpha_composite(a,(x,y+23))
def grid(im,x,y,w,h,step=60):
 d=ImageDraw.Draw(im)
 for xx in range(x,x+w,step): d.line((xx,y,xx,y+h),fill=C['ink'],width=2)
 for yy in range(y,y+h,step): d.line((x,yy,x+w,yy),fill=C['ink'],width=2)

def frame(n):
 t=n/FPS
 if t<2.3:
  u=t;im=Image.new('RGBA',(W,H),C['paper']);d=ImageDraw.Draw(im);d.polygon([(690,0),(W,0),(W,H),(170,H)],fill=C['aqua']); grid(im,770,170,340,500)
  chip(im,'NOIZ / WIRELESS EARBUDS',70,150,'purple',angle=2,size=32)
  dx=int(1100*(1-ease(u/.48)))
  fit(im,'CUT THE',65-dx,295,900,195,'paper',6,True);fit(im,'CORD.',65+dx,500,880,250,'yellow',6,True)
  prod(im,540,1090+int(700*(1-ease((u-.1)/.55))),870+30*math.sin(t*2),-4+2*math.sin(t*2))
  chip(im,'GOODBYE, TANGLES.',120,1500,'pink',angle=-4,size=44)
 elif t<4.7:
  u=t-2.3; im=Image.new('RGBA',(W,H),C['pink']);d=ImageDraw.Draw(im)
  for yy in range(80,H,26):
   for xx in range(0,W,26): d.ellipse((xx,yy,xx+3,yy+3),fill='#a31970')
  chip(im,'SIDE A / YOUR DAILY SOUNDTRACK',65,150,'ink','aqua',2,28)
  dx=int(1100*(1-ease(u/.45)));fit(im,'ZERO',70-dx,315,900,235,'yellow',6,True);fit(im,'WIRES.',70+dx,560,900,235,'paper',6,True)
  prod(im,540+40*math.sin(u*1.3),1125,850,-7+4*math.sin(u*1.5))
  chip(im,'ALL YOU.',275,1495,'aqua','ink',6,66)
 elif t<7.2:
  u=t-4.7; im=Image.new('RGBA',(W,H),C['purple']);d=ImageDraw.Draw(im);grid(im,-20,0,1140,H,80)
  put(im,'PRESS PLAY.',68,165,135,'yellow',5,shadow=True)
  # Retro browser frame follows the repository's fake-window / window-title treatment.
  d.rectangle((78,415,1022,1500),fill=C['ink']);d.rectangle((60,395,1000,1480),fill='#c0c0c0',outline=C['ink'],width=6)
  d.rectangle((72,407,988,477),fill='#000080');put(im,'NOIZ.EXE / NOW PLAYING',90,422,31,'paper',mono=True);put(im,'_  X',850,422,31,'paper',mono=True)
  d.rectangle((82,490,978,1455),fill=C['paper'],outline=C['ink'],width=3)
  chip(im,'SMALL BUDS.',150,535,'yellow','ink',-3,53)
  prod(im,540,995,720,2*math.sin(u*2))
  for j in range(19):
   ht=20+65*abs(math.sin(u*7+j*.9));x=145+j*42;d.rectangle((x,1380-ht,x+27,1380),fill=C['purple'] if j%2 else C['pink'])
  chip(im,'BIG ENERGY.',215,1505,'pink','paper',-3,62)
 else:
  u=t-7.2;im=Image.new('RGBA',(W,H),C['yellow']);d=ImageDraw.Draw(im)
  chip(im,'WIRELESS EARBUDS / REMIX YOUR DAY',62,150,'ink','aqua',1,28)
  sc=ease(u/.45); fit(im,'NOIZ',60,285+int(160*(1-sc)),940,340,'paper',8,True)
  prod(im,540,1030,850+16*math.sin(u*2),-2+2*math.sin(u*1.5))
  put(im,'YOUR WORLD.',82,1470,81,'ink');put(im,'ON REPEAT.',82,1560,81,'ink')
  chip(im,'FIND YOUR FREQUENCY.',68,1690,'pink','paper',-2,39)
 if t<7.2:ticker(im,t)
 # Consistent safe footer. Concept label avoids suggesting a real purchasable product.
 put(im,'NOIZ  /  ORIGINAL CONCEPT AD',65,1818,27,'ink' if t<2.3 or t>=7.2 else 'paper',mono=True)
 # Fast editorial wipe at scene changes; typography is readable for the hold afterward.
 for cut in (2.3,4.7,7.2):
  if cut<=t<cut+.18:
   x=int(W*((t-cut)/.18));ImageDraw.Draw(im).rectangle((x,0,W,H),fill=C['aqua'])
 return im.convert('RGB')

def soundtrack(path):
 sr=48000; N=sr*10; a=np.zeros((N,2),np.float64);rng=np.random.default_rng(90)
 def add(t,dur,fn,vol=1,pan=0):
  start=int(t*sr);cnt=min(int(dur*sr),N-start)
  if cnt<=0:return
  q=np.arange(cnt)/sr;v=fn(q)*vol;a[start:start+cnt,0]+=v*(1-pan*.5);a[start:start+cnt,1]+=v*(1+pan*.5)
 for b in range(20):
  bt=b*.5
  add(bt,.34,lambda q:np.sin(2*np.pi*(49*q+2.4*(1-np.exp(-q*35))))*np.exp(-q*18),.68)
  if b%2: add(bt,.2,lambda q:(rng.normal(size=q.size)*.7+np.sin(2*np.pi*180*q)*.3)*np.exp(-q*28),.25)
  for off in (0,.25):add(bt+off,.065,lambda q:rng.normal(size=q.size)*np.exp(-q*70),.075,(-1)**b*.5)
  note=[55,55,65.406,49][(b//2)%4]
  add(bt+.125,.28,lambda q,f=note:(np.sin(2*np.pi*f*q)+.2*np.sin(4*np.pi*f*q))*np.sin(np.pi*np.minimum(q/.28,1))**2,.2)
 for bt in (0,2.3,4.7,7.2):
  add(bt,.65,lambda q:sum(np.sin(2*np.pi*f*q) for f in (220,261.626,329.628))*np.exp(-q*6)*(1-np.exp(-q*150)),.09)
  add(max(0,bt-.12),.24,lambda q:rng.normal(size=q.size)*np.sin(np.pi*q/.24)**2,.13)
 a=np.tanh(a)*.87;a*=np.minimum(1,np.arange(N)[:,None]/480);a*=np.minimum(1,(N-np.arange(N))[:,None]/7000)
 with wave.open(str(path),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((a*32767).astype('<i2').tobytes())

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--preview',action='store_true');args=ap.parse_args();out=args.output;out.mkdir(parents=True,exist_ok=True)
 for i,n in enumerate((40,105,180,260)):
  im=frame(n);im.save(out/f'NOIZ_frame_{i+1}.jpg',quality=94)
 # Contact sheet with all four complete frames, not overlapping crops.
 sheet=Image.new('RGB',(1080,480))
 for i,n in enumerate((40,105,180,260)):sheet.paste(frame(n).resize((270,480)),(i*270,0))
 sheet.save(out/'NOIZ_storyboard.jpg',quality=95)
 if args.preview:return
 wav=out/'NOIZ_original_soundtrack.wav';soundtrack(wav)
 ff=imageio_ffmpeg.get_ffmpeg_exe();log=open(out/'encode.log','w')
 cmd=[ff,'-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-i',str(wav),'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-t','10','-movflags','+faststart',str(out/'NOIZ_90s_Earbuds_10s.mp4')]
 p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=log)
 for n in range(300):
  p.stdin.write(frame(n).tobytes())
  if n%60==0:print(f'{n}/300 frames',flush=True)
 p.stdin.close();assert p.wait()==0;log.close()
 check=subprocess.run([ff,'-i',str(out/'NOIZ_90s_Earbuds_10s.mp4'),'-f','null','-'],capture_output=True,text=True)
 (out/'verification.txt').write_text(check.stderr);assert check.returncode==0;assert '00:00:10.00' in check.stderr and '1080x1920' in check.stderr and 'frame=  300' in check.stderr
 print('Verified 300 frames / 10 seconds / 1080x1920 / 30 fps / stereo AAC',flush=True)
if __name__=='__main__':main()
