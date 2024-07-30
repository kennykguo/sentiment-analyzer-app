// Import React
import React from 'react';
// Import ReactDOM from react-dom/client for React 18+
import ReactDOM from 'react-dom/client';
// Import the main App component
import App from './App';
// Import BrowserRouter for routing
import { BrowserRouter } from 'react-router-dom';
// Import AuthProvider from your context file
import { AuthProvider } from './contexts/AuthContext';

// Create a root instance to render React elements
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the application
root.render(
    // Wrap the app in StrictMode for additional checks and warnings
    // Wrap the app in BrowserRouter for routing
    // Wrap the app in AuthProvider to provide authentication context
    // Render the main App component
    <React.StrictMode>
        <BrowserRouter>
            <AuthProvider>
                <App />
            </AuthProvider>
        </BrowserRouter>
    </React.StrictMode>
);