export default function Home() {
  return (
    <main>
      <nav className="topbar" aria-label="Primary navigation">
        <a className="logo" href="#top">MODERN? NEVER!</a>
        <div className="navlinks"><a href="#manifesto">MANIFESTO</a><a href="#stuff">COOL STUFF</a><a href="#contact">E-MAIL US</a></div>
      </nav>
      <section className="hero" id="top">
        <div className="grid-fragment" aria-hidden="true" /><div className="pink-slab" aria-hidden="true" />
        <div className="starburst" aria-hidden="true">NEW!</div><div className="chrome-ball" aria-hidden="true" />
        <p className="issue-label">VOL. 96 / ISSUE 01</p>
        <h1><span>WELCOME</span><em>TO THE</em><strong>FUTURE</strong></h1>
        <p className="dek">A maximum-bandwidth transmission from the most optimistic corner of the information superhighway.</p>
        <a className="enter-button" href="#manifesto">[ ENTER THE EXPERIENCE ]</a>
        <div className="pixel-computer" aria-label="A tiny pixel computer"><div className="pixel-screen">HI!</div><div className="pixel-base" /></div>
        <div className="squiggle" aria-hidden="true">∿∿∿</div>
      </section>
      <div className="ticker" aria-label="Site announcements"><div>★ BEST VIEWED WITH YOUR MIND WIDE OPEN ★ 28.8K OF PURE DESIGN ENERGY ★ NO BEIGE STARTUPS ALLOWED ★ BEST VIEWED WITH YOUR MIND WIDE OPEN ★ 28.8K OF PURE DESIGN ENERGY ★</div></div>
      <section className="manifesto" id="manifesto">
        <p className="vertical">DESIGN TRANSMISSION</p>
        <div className="manifesto-title"><span>TOO MUCH</span><br />IS NEVER ENOUGH.</div>
        <div className="manifesto-copy"><p className="mono">/// FILE: MANIFESTO.TXT</p><p>We believe in loud colors, hard edges, heroic typography, and hyperlinks you can actually see.</p><a className="button" href="#stuff">[ WHAT’S NEW? ]</a></div>
      </section>
      <section className="stuff" id="stuff">
        <div className="section-kicker">THE REALLY COOL PART ↓</div>
        <h2>SELECT YOUR<br /><i>DESTINATION</i></h2>
        <div className="portal-grid">
          <a className="portal portal-one" href="#browser"><b>01</b><span>EXPLORE<br />CYBERSPACE</span><small>CLICK HERE →</small></a>
          <a className="portal portal-two" href="#browser"><b>02</b><span>MAKE<br />SOMETHING LOUD</span><small>YES, PLEASE →</small></a>
          <a className="portal portal-three" href="#contact"><b>03</b><span>SEND US<br />ELECTRONIC MAIL</span><small>CONNECT! →</small></a>
        </div><p className="side-note">100% Y2K COMPATIBLE*</p>
      </section>
      <section className="browser-zone" id="browser">
        <div className="fake-window"><div className="window-title"><span>THE_COOL_ZONE.HTML</span><span>_ □ ×</span></div>
          <div className="window-tools"><button type="button">←</button><button type="button">→</button><div>http://www.coolzone.net/~future</div></div>
          <div className="window-body"><p className="blink">WELCOME, WEB TRAVELER!</p>
            <div className="download-box"><strong>DOWNLOAD MORE STYLE</strong><div className="progress"><span /></div><small>96% COMPLETE — ALWAYS</small></div>
            <div className="hotlist"><p>HOT LINKS:</p><a href="#top">★ Back to the future</a><a href="#manifesto">★ Read our beliefs</a><a href="#contact">★ Sign the guestbook</a></div>
          </div></div><div className="stamp">COOL<br />SITE!</div><div className="orbit" aria-hidden="true">✦</div>
      </section>
      <section className="contact" id="contact"><p className="contact-script">Don’t be a stranger!</p><h2>LET’S MAKE<br />THE WEB WEIRD.</h2>
        <a className="email" href="mailto:hello@modern-never.example">[ E-MAIL US NOW ]</a>
        <div className="guestbook">YOU ARE VISITOR <strong>0 0 0 1 9 9 6</strong></div>
        <p className="fineprint">© 1996–FOREVER MODERN? NEVER! / MADE WITH 256 COLORS AND MAXIMUM ENTHUSIASM / BEST VIEWED AT ANY RESOLUTION</p>
      </section>
    </main>
  );
}
