import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return (
        <div>
            <h1>Welcome to Our App</h1>
            <p>Please login or register to continue.</p>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
        </div>
    );
};

export default HomePage;