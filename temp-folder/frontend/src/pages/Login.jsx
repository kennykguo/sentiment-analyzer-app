import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
// import { AppContext } from '../Context';
import api from '../api';
import LoadingIndicator from '../components/LoadingIndicator';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const { login } = useContext(AppContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await api.post('/api/token/', { email, password });
            localStorage.setItem(ACCESS_TOKEN, res.data.access);
            localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
            await login(res.data.user, res.data.company);
            navigate('/dashboard');
        } catch (error) {
            console.error('Login failed:', error);
            setError(error.response?.data?.detail || 'An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="form-container">
            <h1>Login</h1>
            {error && <p className="error">{error}</p>}
            <form onSubmit={handleSubmit}>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                    required
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
                {loading && <LoadingIndicator />}
                <button type="submit" disabled={loading}>Login</button>
            </form>
        </div>
    );
};

export default LoginPage;