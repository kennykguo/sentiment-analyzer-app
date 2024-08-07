import React, { useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContext';

const Header = () => {
    const { user, logout } = useContext(AuthContext);
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    return (
        <header className="bg-gradient-to-r from-[#201E43] to-[#10103f] text-white shadow-md">
            <div className="container mx-auto px-4 py-3">
                <div className="flex justify-between items-center">
                    <div className="flex items-center space-x-8">
                        <Link to="/" className="flex items-center space-x-3">
                            <img className="h-10 w-auto" src="src/assets/logo.jpg" alt="ML4U logo" />
                            <span className="text-xl font-bold text-white">ML4U</span>
                        </Link>
                        <nav className="hidden md:flex items-center space-x-6">
                            <Link to='/' className="text-sm text-white hover:text-[#508C9B] transition duration-300">Home</Link>
                            <Link to='/pricing' className="text-sm text-white hover:text-[#508C9B] transition duration-300">Pricing</Link>
                            <Link to='/about' className="text-sm text-white hover:text-[#508C9B] transition duration-300">About</Link>
                            {user && <Link to='/dashboard' className="text-sm text-white hover:text-[#508C9B] transition duration-300">Dashboard</Link>}
                        </nav>
                    </div>
                    
                    <div className="hidden md:flex items-center space-x-4">
                        {user ? (
                            <>
                                <Link to='/company' className="bg-white text-[#201E43] px-4 py-1.5 rounded-full hover:bg-opacity-80 transition duration-300 text-sm font-semibold">Company</Link>
                                <button onClick={logout} className="bg-[#508C9B] text-white px-4 py-1.5 rounded-full hover:bg-[#134B70] transition duration-300 text-sm font-semibold">Log out</button>
                            </>
                        ) : (
                            <>
                                <Link to='/register' className="bg-[#508C9B] text-white px-4 py-1.5 rounded-full hover:bg-[#134B70] transition duration-300 text-sm font-semibold">Get Started</Link>
                                <Link to='/login' className="bg-transparent hover:bg-white hover:text-[#201E43] text-white px-4 py-1.5 rounded-full border-2 border-white transition duration-300 text-sm font-semibold">Log in</Link>
                            </>
                        )}
                    </div>
                    
                    <button 
                        className="md:hidden text-white focus:outline-none"
                        onClick={() => setIsMenuOpen(!isMenuOpen)}
                    >
                        <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                </div>
                
                {isMenuOpen && (
                    <div className="md:hidden mt-4">
                        <Link to='/' className="block py-2 text-sm text-white hover:text-[#508C9B]">Home</Link>
                        <Link to='/pricing' className="block py-2 text-sm text-white hover:text-[#508C9B]">Pricing</Link>
                        <Link to='/about' className="block py-2 text-sm text-white hover:text-[#508C9B]">About</Link>
                        {user && <Link to='/dashboard' className="block py-2 text-sm text-white hover:text-[#508C9B]">Dashboard</Link>}
                        {user ? (
                            <>
                                <Link to='/company' className="block py-2 text-sm text-white hover:text-[#508C9B]">Company</Link>
                                <button onClick={logout} className="block w-full text-left py-2 text-sm text-[#508C9B] hover:text-[#134B70]">Log out</button>
                            </>
                        ) : (
                            <>
                                <Link to='/register' className="block py-2 text-sm text-[#508C9B] hover:text-[#134B70]">Get Started</Link>
                                <Link to='/login' className="block py-2 text-sm text-white hover:text-[#508C9B]">Log in</Link>
                            </>
                        )}
                    </div>
                )}
            </div>
        </header>
    );
};

export default Header;