export default function Navbar() {
  return (
    <div className="sticky top-0 z-50 backdrop-blur bg-white/5 border-b border-white/10">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        
        <h1 className="text-2xl font-bold tracking-wide">
        UN Votes Analyser
        </h1>

        <div className="flex gap-8 text-sm text-gray-300">
          <span className="hover:text-white cursor-pointer transition">Global Issues</span>
          <span className="hover:text-white cursor-pointer transition">Countries</span>
          <span className="hover:text-white cursor-pointer transition">Compare</span>
        </div>

      </div>
    </div>
  );
}