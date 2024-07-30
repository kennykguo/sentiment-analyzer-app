// import React, { useState } from 'react';
// import Register from './components/Register';
// import Dashboard from './components/Dashboard';

// function App() {
//   const [token, setToken] = useState(null);

//   return (
//     <div className="App">
//       {token ? (
//         <Dashboard token={token} />
//       ) : (
//         <Register setToken={setToken} />
//       )}
//     </div>
//   );
// }

// export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import CompanyPage from './components/CompanyPage';
import PrivateRoute from './components/PrivateRoute';
import RegisterPage from './components/RegisterPage';
import { AppProvider } from './Context';
import './App.css'

const App = () => {
  return (
    <AppProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<HomePage />} />
            <Route path="login" element={<LoginPage />} />
            <Route path="register" element={<RegisterPage />} />
            <Route 
              path="company" 
              element={
                <PrivateRoute>
                  <CompanyPage />
                </PrivateRoute>
              } 
            />
          </Route>
        </Routes>
      </Router>
    </AppProvider>
  );
};

export default App;