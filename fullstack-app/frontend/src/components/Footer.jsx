import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContext';
import './../styles/Footer.css';

const Footer = () => {
    const { user } = useContext(AuthContext);

    return (
        <footer>
            <div className="footer__main">
                {/* <img className="footer__logo" src="/assets/logo.jpg" alt="logo" /> */}
            </div>
            <nav className="footer__nav">
                <p className="footer__copyright">Copyright | &copy;2023<br/>All rights reserved<br/>Web-development</p>
                <Link to='/'>Product</Link>
                {user && <Link to='/analysis'>Statistical Analysis</Link>}
                <Link to='/pricing'>Pricing</Link>
                <Link to='/about'>About</Link>
                <Link to='/about/team'>Our team</Link>
                <Link to='/contact'>Get in touch</Link>
                <Link to='/support'>Support</Link>
                {user && <Link to='/dashboard'>Dashboard</Link>}
            </nav>
        </footer>
    );
};

export default Footer;
