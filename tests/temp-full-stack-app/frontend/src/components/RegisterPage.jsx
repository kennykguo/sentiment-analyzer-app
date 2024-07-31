import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AppContext } from '../Context';


const RegisterPage = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [companyName, setCompanyName] = useState('');
    const [error, setError] = useState('');

    const { register, login } = useContext(AppContext); // Add login here
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            console.log('Registering user...');
            await register(username, email, password, companyName);
            
            await new Promise(resolve => setTimeout(resolve, 2000)); // 2 seconds delay
            
            console.log('Logging in...');
            await login(email, password);
            
            console.log('Navigating to dashboard...');
            navigate('/dashboard');
            
        } catch (error) {
            console.error('Registration/Login failed:', error);
            setError('Registration or login failed. Please try again.');
        }
    };

    return (
        <div className="form-container">
            <h1>Register</h1>
            {error && <p className="error">{error}</p>}
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                />
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                />
                <input
                    type="text"
                    value={companyName}
                    onChange={(e) => setCompanyName(e.target.value)}
                    placeholder="Company Name"
                />
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default RegisterPage;
