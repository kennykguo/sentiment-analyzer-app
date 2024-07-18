// Import React and the useContext hook
import React, { useContext } from 'react';
// Import the AuthContext (make sure this file exists and is properly exported)
import { AuthContext } from '../contexts/AuthContext';

// Define the Home component
const Home = () => {
    // Destructure authTokens and logoutUser from AuthContext
    const { authTokens, logoutUser } = useContext(AuthContext);

    return (
        // Container div
        // Header
        <div>
            <h1>Home</h1>
            {/* Conditional rendering based on authTokens */}
            {authTokens ? (
                // If user is authenticated
                // Logout button
                <>
                    <button onClick={logoutUser}>Logout</button>
                    {/* Add your content here */}
                </>
            ) : (
                // If user is not authenticated
                <p>Please log in</p>
            )}
        </div>
    );
};

// Export the Home component
export default Home;