import React, { useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import LoadingIndicator from '../components/LoadingIndicator';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';
import { AuthContext } from '../AuthContext';
import { jwtDecode } from 'jwt-decode'; // Ensure this import matches your jwt-decode package


const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [companyName, setCompanyName] = useState('');
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
            const response = await api.post('/api/register/', {
                email,
                password,
                company_name: companyName
            });
            console.log('Registration successful:', response.data);
            const decoded = jwtDecode(response.data.access);
            localStorage.setItem(ACCESS_TOKEN, response.data.access);
            localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
            login(decoded);
            navigate('/dashboard');
        } catch (error) {
            console.error('Registration failed:', error);
            setError(error.response?.data?.message || error.response?.data?.error || 'An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="form-container">
            <h1>Register</h1>
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
                <input
                    type="text"
                    value={companyName}
                    onChange={(e) => setCompanyName(e.target.value)}
                    placeholder="Company Name"
                    required
                />
                {loading && <LoadingIndicator />}
                <button type="submit" disabled={loading}>Register</button>
            </form>
        </div>
    );
};

export default Register;
