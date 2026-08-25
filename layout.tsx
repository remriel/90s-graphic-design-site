import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Modern? Never! — A 1996 Design Transmission",
  description: "Loud colors, hard edges, heroic type, and pure information-superhighway optimism.",
  metadataBase: new URL("https://sites.openai.com"),
  openGraph: { title: "Modern? Never!", description: "A 1996 Design Transmission", images: ["/og.png"] },
  twitter: { card: "summary_large_image", title: "Modern? Never!", description: "A 1996 Design Transmission", images: ["/og.png"] },
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
