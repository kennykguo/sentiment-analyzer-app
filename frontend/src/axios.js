// frontend/src/axios.js
import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000/api/', // Django backend URL
});

export default instance;
