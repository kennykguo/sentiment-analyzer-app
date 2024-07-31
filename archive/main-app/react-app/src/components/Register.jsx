// Import React, useContext hook, and useState hook
import React, { useContext, useState } from 'react';
// Import AuthContext (ensure this file exists and is properly exported)
import { AuthContext } from '../contexts/AuthContext';

// Define the Register component
const Register = () => {
    // Destructure registerUser function from AuthContext
    const { registerUser } = useContext(AuthContext);
    // State for username, password, and email
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        await registerUser(username, password, email);
    };

    return (
        // Registration form
        // Username input
        // Password input
        // Email input
        // Submit button
        <form onSubmit={handleSubmit}>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
            <button type="submit">Register</button>
        </form>
    );
};

// Export the Register component
export default Register;