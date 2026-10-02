import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Career Intelligence Platform",
  description: "Deterministic career tracking with advisory AI.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
