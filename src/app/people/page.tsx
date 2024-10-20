// src/app/people/page.tsx
import React from 'react'; // Import React
import { FaLinkedin } from 'react-icons/fa'; // Import LinkedIn icon
import Image from 'next/image'; // Import Next.js Image component
import butter from '@/assets/q.png'; // Correctly import your background image

const teamMembers = [
    {
        name: "Raghav Krishna",
        linkedin: "https://www.linkedin.com/in/raghav-krishna-m-6357bb290/",
        description: "Loves Supercars & <Coding/>",
    },
    {
        name: "Suhail",
        linkedin: "https://www.linkedin.com/in/mohammed-suhail-ahmed-khan-4a753a316/",
        description: "Only Cats ",
    },
    {
        name: "Bhuvan",
        linkedin: "https://www.linkedin.com/in/bhuvan-s-m-99351629a/",
        description: "Director in the making",
    },
    {
        name: "Minhaj",
        linkedin: "https://www.youtube.com/watch?v=2esVV2--CkY",
        description: "The Lunch dude",
    },
    {
        name: "Nahil",
        linkedin: "https://www.linkedin.com/in/nahilrasheed/",
        description: "A good Human",
    },
];

const PeoplePage = () => {
    return (
        <section className="relative h-screen flex items-center justify-center">
            <div className="absolute inset-0 z-0">
                <Image
                    src={butter} // Use the imported image
                    alt="Background"
                    layout="fill" // Makes the image cover the section
                    objectFit="cover" // Maintains aspect ratio
                    priority
                />
            </div>
            {/* Overlay to lighten the background */}
            <div className="absolute inset-0 bg-white opacity-75 z-0" /> {/* Adjust opacity here */}
            <div className="relative w-3/5 max-h-[80vh] border-4 border-black bg-gray-300 shadow-lg flex flex-col overflow-y-auto z-10">
                <div className="bg-blue-800 text-white flex justify-between items-center p-2 border-b-2 border-black font-bold text-xl">
                    <span className="title">The People.</span>
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

                <div className="p-5 flex-grow overflow-y-auto">
                    <table className="min-w-full border-collapse border border-black">
                        <thead>
                            <tr className="bg-gray-200">
                                <th className="border border-black p-2 text-left text-lg font-semibold">Name.</th>
                                <th className="border border-black p-2 text-left text-lg font-semibold">Description.</th>
                                <th className="border border-black p-2 text-left text-lg font-semibold">LinkedIn ID.</th>
                            </tr>
                        </thead>
                        <tbody>
                            {teamMembers.map((member) => (
                                <tr
                                    key={member.name}
                                    className="border-b border-black hover:bg-gray-100 transition duration-300"
                                >
                                    <td className="border border-black p-2">
                                        <strong>{member.name}</strong> {/* Bold the names */}
                                    </td>
                                    <td className="border border-black p-2">{member.description}</td>
                                    <td className="border border-black p-2">
                                        <a
                                            href={member.linkedin}
                                            className="text-blue-600 hover:text-blue-800"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                        >
                                            <FaLinkedin className="inline text-xl" />
                                        </a>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
                <div className="p-2 text-center text-sm text-gray-600 border-t-2 border-black">
                    <p>© Zorenza Radiance. All rights reserved.</p>
                </div>
            </div>
        </section>
    );
};

export default PeoplePage;
