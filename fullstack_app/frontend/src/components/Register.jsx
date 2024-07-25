// src/components/Register.jsx

import React, { useState } from 'react';
import axios from 'axios';

const Register = ({ setToken }) => {
  const [email, setEmail] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send registration data to the backend
      const response = await axios.post('http://localhost:8000/api/register/', {
        email,
        username: email,
        company_name: companyName,
        password,
      });

      // After successful registration, obtain the token
      const tokenResponse = await axios.post('http://localhost:8000/api/token/', {
        username: email,
        password,
      });

      // Set the token in the parent component
      setToken(tokenResponse.data.access);
    } catch (error) {
      console.error('Registration error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        required
      />
      <input
        type="text"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
        placeholder="Company Name"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit">Register</button>
    </form>
  );
};

export default Register;