import React, { useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import LoadingIndicator from '../components/LoadingIndicator';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';
import { AuthContext } from '../AuthContext';
import {jwtDecode} from 'jwt-decode';
import '../index.css';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        const checkAuth = async () => {
            const token = localStorage.getItem(ACCESS_TOKEN);
            if (token) {
                try {
                    const decoded = jwtDecode(token);
                    const now = Date.now() / 1000;
                    if (decoded.exp > now) {
                        login(decoded);
                        navigate('/dashboard');
                    }
                } catch (error) {
                    console.error('Token validation failed:', error);
                }
            }
        };

        checkAuth();
    }, [login, navigate]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await api.post('/api/token/', { email, password });
            localStorage.setItem(ACCESS_TOKEN, res.data.access);
            localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
            const decoded = jwtDecode(res.data.access);
            login(decoded);
            navigate('/dashboard');
        } catch (error) {
            console.error('Login failed:', error);
            setError(error.response?.data?.detail || 'An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-navy-dark to-navy-light">
            <div className="bg-gradient-to-br from-navy-medium to-navy-light p-8 rounded-lg shadow-lg w-full max-w-md transition-all duration-300 ease-in-out">
                <h1 className="text-2xl font-bold text-center mb-6 text-white">Login</h1>
                {error && <p className="text-red-500 text-center mb-4">{error}</p>}
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div className="relative">
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Email"
                            required
                            className="w-full px-4 py-2 bg-navy-dark border border-navy-light rounded-md focus:outline-none focus:border-blue-400 text-white placeholder-gray-400 text-sm"
                        />
                    </div>
                    <div className="relative">
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Password"
                            required
                            className="w-full px-4 py-2 bg-navy-dark border border-navy-light rounded-md focus:outline-none focus:border-blue-400 text-white placeholder-gray-400 text-sm"
                        />
                    </div>
                    <button 
                        type="submit" 
                        disabled={loading}
                        className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition duration-300 ease-in-out text-sm"
                    >
                        Login
                    </button>
                </form>
                {loading && <LoadingIndicator />}
            </div>
        </div>
    );
};

export default Login;