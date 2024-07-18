// Import React
import React from 'react';
// Import Routes and Route components from react-router-dom
import { Routes, Route } from 'react-router-dom';
// Import Home and About components
import Home from './components/Home';
import About from './components/About';
import Login from './components/Login';
import Register from './components/Register';

// Define the App component
function App() {
  return (
    // Set up routes
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/about" element={<About />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

// Export the App component
export default App;