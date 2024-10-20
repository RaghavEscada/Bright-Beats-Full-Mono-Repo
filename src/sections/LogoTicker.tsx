import qa from '@/assets/qa.png';
import Image from 'next/image';

export const L = () => {
  return (
    <section style={{
      display: 'flex',
      alignItems: 'center',
      height: '100vh',
      background: 'linear-gradient(to right, #4facfe, #00f2fe)', // Gradient background
      padding: '20px', // Padding for better layout
      boxSizing: 'border-box' // Ensures padding is included in height calculations
    }}>
      <div style={{ flex: '3', marginRight: '10px' }}> {/* Increased flex value for the image container */}
        <Image
          src={qa}
          alt="Description of the image"
          layout="responsive" // Use responsive layout
          width={1200}       // Set a larger original width
          height={600}       // Set a larger original height
          style={{ maxWidth: '100%', height: 'auto' }} // Ensures it scales correctly
        />
      </div>
      <div style={{ flex: '1', textAlign: 'right' }}> {/* Text aligned to the right */}
        <span style={{ fontSize: '5rem', fontWeight: 'bold', display: 'block' }}>Playground.</span>
        <p className="flex justify-end" style={{ fontSize: '1rem', fontWeight: 'bold' }}>Discover skill verified students with AI.</p>
      </div>
    </section>
  );
};

export default L;
