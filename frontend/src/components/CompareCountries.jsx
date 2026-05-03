import { useState } from "react";
import { compareCountries } from "../services/api";

export default function CompareCountries() {
  const [c1, setC1] = useState("");
  const [c2, setC2] = useState("");
  const [result, setResult] = useState(null);

  const handleCompare = async () => {
    try {
      const res = await compareCountries(c1, c2);
      setResult(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Compare Countries</h2>

      <input
        placeholder="Country 1"
        value={c1}
        onChange={(e) => setC1(e.target.value)}
      />

      <input
        placeholder="Country 2"
        value={c2}
        onChange={(e) => setC2(e.target.value)}
      />

      <button onClick={handleCompare}>Compare</button>

      {result && (
        <div>
          <p>{result.country1} vs {result.country2}</p>
          <p>Agreement: {result.agreement}%</p>
          <p>Total Votes: {result.totalVotes}</p>
        </div>
      )}
    </div>
  );
}