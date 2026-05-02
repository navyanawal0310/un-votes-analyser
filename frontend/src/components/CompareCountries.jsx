import { useState } from "react";
import API from "../api";

export default function CompareCountries() {
  const [c1, setC1] = useState("");
  const [c2, setC2] = useState("");
  const [score, setScore] = useState(null);

  const compare = async () => {
    const res = await API.get(`/compare/${c1}/${c2}`);
    setScore(res.data.alignment_score);
  };

  return (
    <div>
      <h2>Compare Countries</h2>

      <input placeholder="Country 1" onChange={(e) => setC1(e.target.value)} />
      <input placeholder="Country 2" onChange={(e) => setC2(e.target.value)} />

      <button onClick={compare}>Compare</button>

      {score !== null && <h3>Alignment Score: {score}</h3>}
    </div>
  );
}