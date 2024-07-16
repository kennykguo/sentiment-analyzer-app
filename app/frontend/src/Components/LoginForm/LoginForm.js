// frontend/src/Components/LoginForm/LoginForm.js
import React, { useState, useContext } from 'react';
import axios from '../axios';
import { AppContext } from '../../Context';

const LoginForm = () => {
    const [email, setEmail] = useState(''); // State for email
    const [password, setPassword] = useState(''); // State for password
    const { handlerClose } = useContext(AppContext); // Getting handlerClose from context

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('token/', {
                username: email,
                password: password,
            });
            console.log(response.data);
            // Save token and handle login state
            handlerClose(); // Close modal on successful login
        } catch (error) {
            console.error(error); // Log any errors
        }
    };

    return (
        <form onSubmit={handleSubmit}>
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
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginForm;
