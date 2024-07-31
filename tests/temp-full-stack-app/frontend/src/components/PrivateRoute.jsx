import React, { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { AppContext } from '../Context';

const PrivateRoute = () => {
    // Access the isAuthenticated state from AppContext
    const { isAuthenticated } = useContext(AppContext);

    // If authenticated, render the child routes
    // If not, redirect to the login page
    return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
};

export default PrivateRoute;