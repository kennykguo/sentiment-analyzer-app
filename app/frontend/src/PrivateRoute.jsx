import { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AppContext } from './Context';

const PrivateRoute = ({ children }) => {
    const { user } = useContext(AppContext);
    return user ? children : <Navigate to="/login" />;
};

export default PrivateRoute;
