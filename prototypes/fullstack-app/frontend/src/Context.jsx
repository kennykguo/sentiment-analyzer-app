import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000/';
// axios.defaults.headers.post['Content-Type'] = 'application/json';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem('token'));
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        if (token) {
            setIsAuthenticated(true);
            fetchUserData();
        }
    }, [token]);

    const fetchUserData = async () => {
        try {
            const response = await axios.get('/api/user/', {
                headers: { Authorization: `Bearer ${token}` }
            });
            setUser(response.data);
        } catch (error) {
            console.error('Error fetching user data:', error);
            logout();
        }
    };

    const login = async (email, password) => {
        try {
            const response = await axios.post('/api/token/', { email, password });
            const { access, refresh } = response.data;
            setToken(access);
            localStorage.setItem('token', access);
            localStorage.setItem('refreshToken', refresh);
            setIsAuthenticated(true);
            await fetchUserData();
        } 
        catch (error) {
            // console.error('Login error:', error.response?.data || error.message);
            console.error('Login error:', error.response?.data);
            throw error;
        }
    };

    const register = async (username, email, password, companyName) => {
        try {
            const response = await axios.post('/api/register/', {
                username,
                email,
                password,
                company_name: companyName,
            });
            console.log('Registration response:', response.data);
            // Instead of automatically logging in, return the response
            return response.data;
        } catch (error) {
            console.error('Registration error:', error.response?.data || error.message);
            throw error;
        }
    };

    const refreshToken = async () => {
        try {
            const refreshToken = localStorage.getItem('refreshToken');
            const response = await axios.post('/api/token/refresh/', { refresh: refreshToken });
            const { access } = response.data;
            setToken(access);
            localStorage.setItem('token', access);
            return access;
        } catch (error) {
            console.error('Error refreshing token:', error);
            logout();
        }
    };

    const logout = () => {
        setUser(null);
        setToken(null);
        setIsAuthenticated(false);
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
    };

    return (
        <AppContext.Provider value={{ user, isAuthenticated, login, register, logout }}>
            {children}
        </AppContext.Provider>
    );
};
