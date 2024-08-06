import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContext';

const Footer = () => {
    const { user } = useContext(AuthContext);

    return (
        <footer className="bg-gray-800 text-white py-6">
            <div className="container mx-auto px-4">
                {/* <img className="h-8 w-8 mb-4" src="/assets/logo.jpg" alt="logo" /> */}
                <nav className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0 md:space-x-8">
                    <p className="text-sm text-center md:text-left">
                        &copy; 2023 | All rights reserved <br /> Web-development
                    </p>
                    <div className="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-4">
                        <Link to='/' className="hover:underline">Product</Link>
                        {user && <Link to='/analysis' className="hover:underline">Statistical Analysis</Link>}
                        <Link to='/pricing' className="hover:underline">Pricing</Link>
                        <Link to='/about' className="hover:underline">About</Link>
                        <Link to='/about/team' className="hover:underline">Our team</Link>
                        <Link to='/contact' className="hover:underline">Get in touch</Link>
                        <Link to='/support' className="hover:underline">Support</Link>
                        {user && <Link to='/dashboard' className="hover:underline">Dashboard</Link>}
                    </div>
                </nav>
            </div>
        </footer>
    );
};

export default Footer;
