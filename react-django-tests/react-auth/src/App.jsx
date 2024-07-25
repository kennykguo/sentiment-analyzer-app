import Login from "./components/Login";
import AuthProvider from "./hooks/AuthProvider";

function App() {
  return (
    <div className="App">
      <AuthProvider>{<Login/>}</AuthProvider>
    </div>
  );
}

export default App;