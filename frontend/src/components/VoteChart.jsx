import { PieChart, Pie, Cell } from "recharts";

const data = [
  { name: "YES", value: 120 },
  { name: "NO", value: 30 },
  { name: "ABSTAIN", value: 20 },
];

export default function VoteChart() {
  return (
    <div className="bg-white/5 p-4 rounded-2xl border border-white/10">
      <h2 className="mb-4">Voting Distribution</h2>

      <PieChart width={300} height={300}>
        <Pie data={data} dataKey="value" outerRadius={100}>
          <Cell fill="#22c55e" />
          <Cell fill="#ef4444" />
          <Cell fill="#eab308" />
        </Pie>
      </PieChart>
    </div>
  );
}