import Navbar from "./components/Navbar";
import GlobalIssue from "./components/GlobalIssue";
import CountryStance from "./components/CountryStance";
import CompareCountries from "./components/CompareCountries";

function App() {
  return (
    <div className="bg-gradient-to-br from-gray-950 via-gray-900 to-black text-white min-h-screen">
      
      <Navbar />

      <div className="max-w-7xl mx-auto px-6 py-10 space-y-12">
        <GlobalIssue />
        <CountryStance />
        <CompareCountries />
      </div>

    </div>
  );
}

export default App;