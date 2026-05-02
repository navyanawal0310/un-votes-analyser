import CountryStance from "./components/CountryStance";
import CompareCountries from "./components/CompareCountries";
import GlobalIssue from "./components/GlobalIssue";

function App() {
  return (
    <div>
      <h1>UN Votes Analyzer</h1>

      <CountryStance />
      <CompareCountries />
      <GlobalIssue />
    </div>
  );
}

export default App;