import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Layout from './Layout';
import HomePage from './Pages/HomePage';
import LoginPage from './Pages/LoginPage';
import CompanyPage from './Pages/CompanyPage';
import PrivateRoute from './PrivateRoute';

function App() {
    return (
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<HomePage />} />
                <Route path="login" element={<LoginPage />} />
                <Route path="company" element={<PrivateRoute><CompanyPage /></PrivateRoute>} />
            </Route>
        </Routes>
    );
}

export default App;
