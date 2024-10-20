import Link from 'next/link';
import { FaLinkedin, FaInstagram, FaGithub } from 'react-icons/fa';
import { MdEmail } from 'react-icons/md';
import { TextHoverEffect } from "@/components/ui/text-hover-effect";
import { TypewriterEffectSmooth } from "@/components/ui/typewriter-effect";
import { BackgroundLines } from "@/components/ui/background-lines";



export const Footer = () => {
  return (

    <footer className="footer bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 py-10">
      <div className="flex justify-between items-center pl-10 pr-10">
        
        {/* Left Side: Tagline and Company Name */}
        <div className="flex flex-col">
          <div className="text-[110px] font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-300 tracking-tight text-left">
            <a href="https://www.linkedin.com/company/zorenza-radiance-co/?viewAsMember=true">
              Bright Beats.
            </a>
          </div>
          <div className="text-[30px] font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-300 tracking-tight text-left">
            Connections made easy! 🏆
          </div>
        </div>

        {/* Right Side: Social Media Icons with Links */}
        <div className="flex items-center space-x-8 text-4xl text-white">
          <a href="https://www.linkedin.com/company/zorenza-radiance-co/?viewAsMember=true" target="_blank" rel="noopener noreferrer">
            <FaLinkedin />
          </a>
          <a href="https://github.com/your-github-handle" target="_blank" rel="noopener noreferrer">
            <FaGithub />
          </a>
          <a href="https://www.instagram.com/your-instagram-handle" target="_blank" rel="noopener noreferrer">
            <FaInstagram />
          </a>
          <a href="mailto:info@zorenza.com">
            <MdEmail />
          </a>
        </div>
      </div>

      {/* Footer Bottom Info */}
      {/* <div className="flex justify-center text-white mt-12">
        <p className="text-sm">© 2024 Zorenza Radiance & Co. All rights reserved.</p>
      </div> */}

    
      
    </footer>
  );
};

export default Footer;
