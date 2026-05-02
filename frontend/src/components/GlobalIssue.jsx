import { useState } from "react";
import API from "../api";

export default function GlobalIssue() {
  const [issue, setIssue] = useState("");
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const res = await API.get(`/global/${issue}`);
    setData(res.data.distribution);
  };

  return (
    <div>
      <h2>Global Issue</h2>

      <input
        placeholder="Enter issue (NUCLEAR, etc)"
        onChange={(e) => setIssue(e.target.value)}
      />

      <button onClick={fetchData}>Analyze</button>

      <ul>
        {data.map((d, i) => (
          <li key={i}>
            {d.vote}: {d.count}
          </li>
        ))}
      </ul>
    </div>
  );
}