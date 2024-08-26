
import './globals.css'
import { Metadata } from 'next';
import NavBar from '@/components/NavBar'
import SideMenu from '@/components/SideMenu'

import { Inter } from 'next/font/google'
 

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full dark">
      <body className={`${inter.className} bg-primary-gray text-white-100 flex flex-col h-full`} >
        <NavBar/>
        <div className="flex flex-row h-full w-full">
          <SideMenu/>
          <div className="m-4 flex flex-row w-full h-full">
            {children}
          </div>
        </div>
      </body>
    </html>
  );
}
