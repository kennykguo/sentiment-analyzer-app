// Import necessary React hooks and axios for HTTP requests
import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

// Create a new context for authentication
const AuthContext = createContext();

// Define the AuthProvider component
const AuthProvider = ({ children }) => {
    // Initialize authTokens state, retrieving from localStorage if available
    const [authTokens, setAuthTokens] = useState(() =>
        localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null
    );

    // Function to handle user login
    const loginUser = async (username, password) => {
        // Send POST request to Django backend login endpoint
        const response = await axios.post('http://localhost:8000/accounts/login/', {
            username,
            password,
        });
        // If login is successful (status 200)
        if (response.status === 200) {
            // Set auth tokens in state and localStorage
            setAuthTokens(response.data);
            localStorage.setItem('authTokens', JSON.stringify(response.data));
        }
    };

    // Function to handle user registration
    const registerUser = async (username, password, email) => {
        // Send POST request to Django backend registration endpoint
        const response = await axios.post('http://localhost:8000/accounts/register/', {
            username,
            password,
            email,
        });
        // If registration is successful (status 201)
        if (response.status === 201) {
            // Log in the user after successful registration
            loginUser(username, password);
        }
    };

    // Function to handle user logout
    const logoutUser = () => {
        // Clear auth tokens from state and localStorage
        setAuthTokens(null);
        localStorage.removeItem('authTokens');
    };

    // Provide the AuthContext to child components
    return (
        <AuthContext.Provider value={{ authTokens, loginUser, registerUser, logoutUser }}>
            {children}
        </AuthContext.Provider>
    );
};

// Export the AuthContext and AuthProvider
export { AuthContext, AuthProvider };