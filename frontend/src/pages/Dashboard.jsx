
import FilterPanel from "../components/FilterPanel";
import VoteTable from "../components/VoteTable";
import VoteChart from "../components/VoteChart";

export default function Dashboard() {
  return (
    <div className="p-6 space-y-6">
      
      <h1 className="text-3xl font-bold">
        UN Votes Analyser
      </h1>

      <FilterPanel />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <VoteTable />
        <VoteChart />
      </div>

    </div>
  );
}