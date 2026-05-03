export default function VoteTable({ votes }) {
  if (!votes.length) return <p>No data</p>;

  return (
    <div>
      <h3>Voting Distribution</h3>

      {votes.map((v, i) => (
        <p key={i}>
          {v.vote}: {v.count}
        </p>
      ))}
    </div>
  );
}