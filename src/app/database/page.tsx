import Image from 'next/image';
import xd from '@/assets/xd.jpeg';
import wd from '@/assets/wd.jpeg';

const DbPage = () => {
  return (
    <section className="flex justify-center items-center pt-32 py-10">
      <div className="flex space-x-8">
        <div className="w-1/2">
          <Image src={xd} alt="Description of the image" className="rounded-lg shadow-lg" />
        </div>
        <div className="w-1/2">
          <Image src={wd} alt="Description of the image" className="rounded-lg shadow-lg" />
        </div>

      </div>
      
     
      

    </section>

  );
};

export default DbPage;
