"use client";

import Image from "next/image";
import People from "@/assets/x.jpeg";
import React from "react";


import { motion } from "framer-motion";





export const Hero = () => {
  const techStackTexts = [
    "Next.js",
    "React.js",
    "Streamlit",
    "Groq Cloud",
    "Tkinter",
    "PyMySql",
    "MySQL Workbench",
  ];

  return (
    <section className="pt-[50px]">
      <div className="md:flex">
        <div className="container">
          <h1 className="text-9xl flex pt-32 pb-5 font-bold tracking-tighter bg-gradient-to-tl from-[#50C878] to-[#0F52BA] text-transparent bg-clip-text">
            Bright Beats.
          </h1>
          <p className="flex justify-between text-balance text-3xl text-black tracking-tighter">


          
          Instant student-mentor connections powered by AI.
          </p>

          <div className="pt-8 flex flex-row space-x-4">
            <button className="border rounded-lg flex justify-center px-10 py-3 text-2xl bg-green-500 text-white font-bold hover:bg-green-700">
              Enter Playground
            </button>
            <a href="https://tally.so/r/w5qK7Q" target="_blank" rel="noopener noreferrer">
              <button className="border rounded-lg flex justify-center px-10 py-3 text-2xl bg-sky-500 text-white font-bold hover:bg-sky-700">
                Become a Student Mentor
              </button>
            </a>

          </div>
        </div>

        <div>
          <Image src={People} alt="Description of the image" />
        </div>
      </div>
      <div className="pt-10 pb-0">
        =================================================================================================================================================================================
        </div>

      <div className="flex justify-center font-bold pt-20 text-[67px]">
        Tech stack.
      </div>
      <div className="flex justify-center">
        +==========================================+
        </div>

      {/* Infinite Scrolling Texts */}
      <div className="overflow-hidden relative h-20 mt-8">
        <motion.div
          className="flex justify-start items-center gap-10 pr-9 pl-9 whitespace-nowrap"
          animate={{ x: ["0%", "-100%"] }} // Move left infinitely
          transition={{
            duration: 10, // Adjust speed to control scrolling speed
            ease: "linear",
            repeat: Infinity, // Infinite loop
          }}
        >
          {/* Duplicate techStackTexts multiple times for seamless infinite loop */}
          {[...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts, ...techStackTexts].map(
            (tech, index) => (
              <div
                key={index}
                className="text-3xl font-semibold text-gray-800 dark:text-white"
              >
                {tech}
              </div>
            )
          )}
        </motion.div>
      </div>
    </section>
  );
};

export default Hero;
