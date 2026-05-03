export default function CountryCard({ country }) {
  return (
    <div className="bg-white/5 backdrop-blur p-4 rounded-2xl border border-white/10 hover:scale-105 transition">
      
      <h3 className="text-lg font-semibold">
        {country || "Country"}
      </h3>

      <p className="text-sm text-gray-400">
        Voting Pattern
      </p>

      <div className="mt-2 text-green-400 text-sm">
        Alignment: 78%
      </div>

    </div>
  );
}