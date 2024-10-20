"use client"; // Ensure this is included at the top

import ArrowRight from "@/assets/arrow-right.svg";
import Logo from "@/assets/logosaas.png";
import Image from "next/image";
import Menu from "@mui/icons-material/Menu";
import Close from "@mui/icons-material/Close";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { motion, useScroll } from "framer-motion";

export const Header = () => {
  const { scrollYProgress } = useScroll();
  const router = useRouter();
  const [menuOpen, setMenuOpen] = useState(false);

  const handleLogin = () => {
    router.push("/login");
  };

  const handleWorkflow = () => {
    router.push("/workflow");
  };

  const handleAbout = () => {
    router.push("/about");
  };

  const handlePeople = () => {
    router.push("/people");
  };

  const handleDB = () => {
    router.push("/database");
  };

  const handlegit = () => {
    // Open GitHub and YouTube in separate tabs
    window.open("https://github.com/your-repo-url", "_blank");
    window.open("https://youtube.com/your-video-url", "_blank");
  };

  const toggleMenu = () => {
    setMenuOpen((prev) => !prev);
  };

  return (
    <header className="sticky top-0 backdrop-blur-sm z-0">
      {/* Top banner */}
      <div className="flex justify-center items-center bg-gray-900  py-3">
        <div>
          <p className="inline-flex text-white font-bold items-center gap-1">
            TEAM 10 - DBMS PROJECT
          </p>
          <p className="text-white">+=====================+</p>
        </div>
      </div>

      {/* Progress bar */}
      <motion.div
        className="h-2 bg-gradient-to-r from-purple-600 via-pink-500 to-pink-900 origin-left"
        style={{ scaleX: scrollYProgress }}
      />

      {/* Main header */}
      <div className="py-5 transition-transform duration-300 ease-in-out hover:scale-110">
        <div className="container mx-auto">
          <div className="flex justify-between items-center">
            {/* Logo Link */}
            <Link href="/" className="flex items-center">
              <Image src={Logo} alt="people logo" height={40} width={40} />
            </Link>

            {/* Hamburger menu for mobile */}
            <div className="md:hidden">
              <Menu className="h-5 w-5 cursor-pointer" onClick={toggleMenu} />
            </div>

            {/* Desktop navigation */}
            <nav className="hidden md:flex items-center gap-20 bg-transparent">
              <button 
                onClick={handleAbout}
                className="font-bold text-lg transition-transform duration-200 ease-in-out hover:scale-125"
              >
                About
              </button>
              <button 
                onClick={handlePeople} 
                className="font-bold text-lg transition-transform duration-200 ease-in-out hover:scale-125"
              >
                Developers
              </button>
              <button 
                onClick={handleDB} 
                className="font-bold text-lg transition-transform duration-200 ease-in-out hover:scale-125"
              >
                Database Structure
              </button>
              <button 
                onClick={() => window.open('https://github.com/RaghavEscada/zBond', '_blank')} 
                className="font-bold text-lg transition-transform duration-200 ease-in-out hover:scale-125"
              >
                Github
              </button>
              <button
                onClick={handleLogin}
                className="font-bold text-white text-lg border rounded-lg px-5 py-3 bg-black hover:bg-gray-800 transition-transform duration-200 ease-in-out hover:scale-125"
              >
                Get in Touch
              </button>
            </nav>
          </div>
          
        </div>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div className="md:hidden fixed inset-0 bg-black text-white flex flex-col justify-center items-center z-50">
          <div className="flex flex-col items-center gap-6 w-full px-4">
            <div className="flex justify-between items-center w-full">
              <h2 className="font-bold text-lg">Menu</h2>
              <Close className="h-5 w-5 cursor-pointer" onClick={toggleMenu} />
            </div>
            <Link href="/about" className="font-bold text-xl hover:scale-105 transition-transform duration-200 ease-in-out" onClick={toggleMenu}>
              About
            </Link>
            <Link href="/people" className="font-bold text-xl hover:scale-105 transition-transform duration-200 ease-in-out" onClick={toggleMenu}>
              People
            </Link>
            <Link href="/database" className="font-bold text-xl hover:scale-105 transition-transform duration-200 ease-in-out" onClick={toggleMenu}>
              Database Structure
            </Link>
            <Link href="/workflow" className="font-bold text-xl hover:scale-105 transition-transform duration-200 ease-in-out" onClick={toggleMenu}>
              Workflow
            </Link>
            <Link href="/login" className="font-bold text-xl hover:scale-105 transition-transform duration-200 ease-in-out" onClick={toggleMenu}>
              Login
            </Link>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;
