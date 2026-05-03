import { useState } from "react";
import { getCountry } from "../services/api";

export default function CountryStance() {
  const [country, setCountry] = useState("");
  const [data, setData] = useState(null);

  const handleSearch = async () => {
    try {
      const res = await getCountry(country);
      setData(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Country Stance</h2>

      <input
        placeholder="Enter country"
        value={country}
        onChange={(e) => setCountry(e.target.value)}
      />

      <button onClick={handleSearch}>Search</button>

      {data && (
        <div>
          <p>{country}</p>
          <p>Alignment: {data.alignment}%</p>
        </div>
      )}
    </div>
  );
}