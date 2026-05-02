import { useState } from "react";
import API from "../api";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend } from "recharts";

export default function CountryStance() {
  const [country, setCountry] = useState("");
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const res = await API.get(`/country/${country}`);
    setData(res.data.stance);
  };

  return (
    <div>
      <h2>Country Stance</h2>

      <input
        placeholder="Enter country"
        value={country}
        onChange={(e) => setCountry(e.target.value)}
      />

      <button onClick={fetchData}>Analyze</button>

      <BarChart width={500} height={300} data={data}>
        <XAxis dataKey="issue_name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="YES" fill="#4CAF50" />
        <Bar dataKey="NO" fill="#F44336" />
        <Bar dataKey="ABSTAIN" fill="#FFC107" />
      </BarChart>
    </div>
  );
}