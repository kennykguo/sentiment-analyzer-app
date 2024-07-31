import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AppContext } from '../Context';
import '../styles/Header.css'

const Header = () => {
    // Access the User object and logout function from AppContext
    // Checks if a user is logged in, and provide the log out functionality if necessary
    const { user, logout } = useContext(AppContext);
    
    return (
        <header>
            {/* <img className="header__logo" src="/assets/logo.jpg" alt="logo" /> */}
            <nav className="navigation">
                <Link to='/'>Home</Link>
                <Link to='/pricing'>Pricing</Link>
                <Link to='/about'>About</Link>
            </nav>
            <div className="wrapp__buttons">
                {user ? (
                    <>
                        <Link to='/company' className="btn__try">Dashboard</Link>
                        <button className="btn__login" onClick={logout}>Log out</button>
                    </>
                ) : (
                    <>
                        <Link to='/register' className="btn__try">Register</Link>
                        <Link to='/login' className="btn__login">Log in</Link>
                    </>
                )}
            </div>
        </header>
    );
};

export default Header;