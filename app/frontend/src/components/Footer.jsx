import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContext';

const Footer = () => {
    const { user } = useContext(AuthContext);

    return (
        <footer className="bg-gradient-to-r from-[#201E43] to-[#134B70] text-white py-8">
            <div className="container mx-auto px-4">
                <div className="flex flex-col md:flex-row justify-between items-center space-y-6 md:space-y-0">
                    <div className="flex flex-col items-center md:items-start">
                        <img className="h-12 w-auto mb-4" src="src/assets/logo.jpg" alt="ML4U logo" />
                        <p className="text-sm text-center md:text-left">
                            &copy; 2023 ML4U | All rights reserved <br /> AI-driven solutions
                        </p>
                    </div>
                    <nav className="flex flex-wrap justify-center md:justify-end gap-4">
                        <Link to='/' className="hover:text-[#508C9B] transition duration-300">Home</Link>
                        <Link to='/pricing' className="hover:text-[#508C9B] transition duration-300">Pricing</Link>
                        <Link to='/about' className="hover:text-[#508C9B] transition duration-300">About</Link>
                        {user && <Link to='/dashboard' className="hover:text-[#508C9B] transition duration-300">Dashboard</Link>}
                        {user && <Link to='/analysis' className="hover:text-[#508C9B] transition duration-300">Analysis</Link>}
                        <Link to='/contact' className="hover:text-[#508C9B] transition duration-300">Contact</Link>
                        <Link to='/support' className="hover:text-[#508C9B] transition duration-300">Support</Link>
                    </nav>
                </div>
            </div>
        </footer>
    );
};

export default Footer;