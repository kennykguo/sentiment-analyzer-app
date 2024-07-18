// Import React, useContext hook, and useState hook
import React, { useContext, useState } from 'react';
// Import AuthContext (ensure this file exists and is properly exported)
import { AuthContext } from '../contexts/AuthContext';

// Define the Login component
const Login = () => {
    // Destructure loginUser function from AuthContext
    const { loginUser } = useContext(AuthContext);
    // State for username and password
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    // Handle form submission
    // Triggers an event from AuthContext
    const handleSubmit = async (e) => {
        e.preventDefault();
        await loginUser(username, password);
    };

    return (
        // Login form
        // Functionality for dissapearing text when the user types in something
        // Username input
        // Password input
        // Submit button
        <form onSubmit={handleSubmit}>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
            <button type="submit">Login</button>
        </form>
    );
};

// Export the Login component
export default Login;