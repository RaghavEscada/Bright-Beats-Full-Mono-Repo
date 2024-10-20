"use client";

import React, { useState } from 'react';
import Image from 'next/image';
import backgroundImage from '@/assets/q.png'; // No need for '@/assets/q.png'

const AboutPage = () => {
  const [maximized, setMaximized] = useState(false);

  const toggleMaximize = () => {
    setMaximized(!maximized);
  };

  return (
    <div className="relative w-full h-screen">
      {/* Background Image */}
      <div className="absolute top-0 left-0 w-full h-full z-[-10]">
        <Image
          src={backgroundImage} // Use the imported image
          alt="Background"
          layout="fill" // Makes the image cover the section
          objectFit="cover" // Maintains aspect ratio
          priority
        />
      </div>
      {/* Overlay to lighten the background */}

      <div className="pl-3">⬆️</div>
      <div>Click to go back</div>
      <div className="absolute inset-0 bg-white opacity-75 z-0" /> {/* Adjust opacity here */}

      <div className="flex justify-center pt-5 pb-20">
        <div className="relative w-3/5 max-h-[80vh] border-4 border-black bg-gray-300 shadow-lg flex flex-col overflow-y-auto z-10">
          <div className="bg-blue-800 text-white flex justify-between items-center p-2 border-b-2 border-black font-bold text-lg">
            <span className="title">About Z-Bond.</span>
            <div className="flex">
              <div className="flex space-x-2">
                <button className="bg-green-500 border-2 gap-x-2 border-black text-white cursor-pointer p-1 rounded hover:bg-green-600 transition">
                  ☐
                </button>
                <button className="bg-yellow-500 border-2 border-black text-white cursor-pointer p-1 rounded hover:bg-yellow-600 transition">
                  -
                </button>
                <button className="bg-red-500 border-2 border-black text-white cursor-pointer p-1 rounded hover:bg-red-600 transition">
                  X
                </button>
              </div>
            </div>
          </div>
          <div className="p-5 flex-grow overflow-y-auto">
            <h2 className="text-2xl font-bold mt-2">Join Us</h2>
            <p className="text-lg leading-relaxed">
              Join the <strong>Z-Bond</strong> community today and connect with talented individuals.
            </p>
            <p>
              <a href="" className="text-blue-600 font-bold text-1xl underline animate-pulsen hover:text-red-600 active:bg-blue-500">
              Click to Join
              </a>.
            </p>

            <div className="border-t-2 border-black my-5" />

            <h2 className="text-2xl font-bold mt-2">Our Mission</h2>
            <p className="text-lg leading-relaxed">
            Our platform connects students with faculty-selected, qualified peers for mentorship and collaboration. By providing access to LinkedIn and GitHub profiles, we facilitate seamless communication and networking. Together, we empower students to thrive through meaningful connections and opportunities.
            </p>

            <div className="border-t-2 border-black my-5" />

           



            <h2 className="text-2xl font-bold mt-2">What We Do</h2>
            <p className="text-lg leading-relaxed">
              An AI-driven platform for skill-based connections and collaboration.
            </p>

            <div className="border-t-2 border-black my-5" />

            {/* New Section Below the Text Box */}
            <div className="bg-gray-200 p-5 mt-5 rounded shadow-md">
              <h2 className="text-2xl font-bold mb-2">Get in Touch</h2>
              <p className="text-lg leading-relaxed">
                We would love to hear from you! Whether you have a question, feedback, or just want to connect, reach out to us.
              </p>
              <form className="mt-4">
                <div className="flex flex-col mb-4">
                  <label htmlFor="name" className="mb-1 font-semibold">Your Name:</label>
                  <input type="text" id="name" className="border rounded p-2" required />
                </div>
                <div className="flex flex-col mb-4">
                  <label htmlFor="email" className="mb-1 font-semibold">Your Email:</label>
                  <input type="email" id="email" className="border rounded p-2" required />
                </div>
                <div className="flex flex-col mb-4">
                  <label htmlFor="message" className="mb-1 font-semibold">Your Message:</label>
                  <textarea id="message" className="border rounded p-2" required></textarea>
                </div>
                <button type="submit" className="bg-blue-600 text-white rounded p-2 hover:bg-blue-700 transition">
                  Send Message
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
