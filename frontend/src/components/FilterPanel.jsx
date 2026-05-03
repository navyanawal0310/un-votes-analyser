export default function FilterPanel() {
  return (
    <div className="bg-white/5 backdrop-blur border border-white/10 rounded-2xl p-4 flex flex-wrap gap-4 items-center">
      
      <input
        className="bg-black/40 px-4 py-2 rounded-lg outline-none"
        placeholder="Search Country"
      />

      <select className="bg-black/40 px-4 py-2 rounded-lg">
        <option>All Votes</option>
        <option>YES</option>
        <option>NO</option>
        <option>ABSTAIN</option>
      </select>

      <button className="bg-blue-600 hover:bg-blue-500 px-4 py-2 rounded-lg transition">
        Apply
      </button>

    </div>
  );
}