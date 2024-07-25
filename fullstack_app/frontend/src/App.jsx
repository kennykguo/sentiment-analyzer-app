import React, { useState } from 'react';
import Register from './components/Register';
import Dashboard from './components/Dashboard';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      {token ? (
        <Dashboard token={token} />
      ) : (
        <Register setToken={setToken} />
      )}
    </div>
  );
}

export default App;