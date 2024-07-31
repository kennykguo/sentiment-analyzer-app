import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContext';

const Header = () => {
    const { user, logout } = useContext(AuthContext);

    return (
        <header>
            <img className="header__logo" src="/assets/logo.jpg" alt="logo" />
            <nav className="navigation">
                <Link to='/'>Home</Link>
                <Link to='/pricing'>Pricing</Link>
                <Link to='/about'>About</Link>
                {user && <Link to='/dashboard'>Dashboard</Link>}
            </nav>
            <div className="wrapp__buttons">
                {user ? (
                    <>
                        <Link to='/company' className="btn__try">Company</Link>
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