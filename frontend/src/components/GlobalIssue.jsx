import { useState } from "react";
import { getGlobalIssue } from "../services/api";
import VoteTable from "./VoteTable";

export default function GlobalIssue() {
  const [issue, setIssue] = useState("");
  const [votes, setVotes] = useState([]);

  const handleSearch = async () => {
  try {
    const res = await getGlobalIssue(issue.toLowerCase());
    console.log(res.data);
    const distribution = res.data.distribution;
    const formatted = Object.entries(distribution).map(([vote, count]) => ({
    vote,
    count
    }));
setVotes(formatted);
  } catch (err) {
    console.error(err);
    setVotes([]);
  }
};

  return (
    <div>
      <h2>Global Issue</h2>

      <input
        placeholder="Enter issue (e.g. Ukraine)"
        value={issue}
        onChange={(e) => setIssue(e.target.value)}
      />

      <button onClick={handleSearch}>Search</button>

      <VoteTable votes={votes} />
    </div>
  );
}