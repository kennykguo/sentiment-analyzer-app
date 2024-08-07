import React from 'react';
import { Link } from 'react-router-dom';
import '../index.css';

function NotFound() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-[#201E43] to-[#134B70] text-white flex items-center justify-center">
            <div className="text-center">
                <h1 className="text-6xl font-bold mb-4">404</h1>
                <h2 className="text-3xl font-semibold mb-6">Page Not Found</h2>
                <p className="text-xl mb-8">The page you're looking for doesn't exist!</p>
                <Link to="/" className="bg-[#508C9B] hover:bg-[#134B70] text-white font-bold py-3 px-6 rounded-full transition duration-300">
                    Go Home
                </Link>
            </div>
        </div>
    );
}

export default NotFound;