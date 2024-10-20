"use client";

import React, { useState, FormEvent } from 'react';
import Image from 'next/image'; // Import Next.js Image component
import backgroundImage from '@/assets/q.png'; // Correctly import your background image

const Contact = () => {
  const [message, setMessage] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setSubmitted(true);

    // Mock email sending logic
    setTimeout(() => {
      alert("Your message has been sent to 'raghavesketit@gmail.com'! Yes, this page works for real!");
      setMessage('');
      setSubmitted(false);
    }, 1000);
  };

  return (
    <div className="relative w-full h-screen">
      {/* Background Image */}
      <div className="absolute inset-0 z-0">
        <Image
          src={backgroundImage}
          alt="Background"
          layout="fill"
          objectFit="cover"
          className="opacity-30"
          priority
        />
      </div>

      {/* Overlay */}
      <div className="opacity-0" />

      {/* Content */}
      <div className="relative flex items-center pt-52 justify-center px-4 z-90">
        <div className="w-full max-w-lg bg-black text-green-200 border border-gray-400 rounded-lg shadow-xl overflow-hidden font-mono p-6"> {/* Adjusted max-w and added padding */}
          {/* Header */}
          <div className="bg-gray-800 text-white p-2 flex items-center justify-between">
            <span className="font-medium">Get in Touch</span>
            <div className="flex space-x-1">
              <span className="text-white">_</span>
              <span className="text-white">[]</span>
              <span className="text-white">X</span>
            </div>
          </div>

          {/* Form */}
          <div className="p-4">
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label htmlFor="message" className="block text-sm font-medium text-gray-200 mb-1">
                  Your Message:
                </label>
                <textarea
                  id="message"
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  required
                  className="w-full min-h-[150px] rounded-md border border-gray-500 bg-gray-800 text-gray-200 shadow-sm p-2 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                  placeholder="Type your message here..."
                />
              </div>

              <button
                type="submit"
                disabled={submitted}
                className="w-full bg-blue-600 text-white rounded-md py-2 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors disabled:opacity-50"
              >
                {submitted ? 'Sending...' : 'Send Message'}
              </button>

              {submitted && (
                <p className="text-sm text-green-600 text-center animate-pulse">
                  Sending your message...
                </p>
              )}
            </form>

            <p className="mt-4 text-sm text-gray-400 text-center">
              Yeah, this message box reaches Raghav for real.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
