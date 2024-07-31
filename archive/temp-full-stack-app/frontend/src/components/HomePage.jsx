import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/HomePage.css'

const HomePage = () => {
    return (
        <div className='home__container'>
            <div className="home__context">
                <h1 className='home__title'>AI-Powered<br/> Customer Feedback<br/> Analytics</h1>
                <p className='home__descr'>Want to understand what your customers say in support calls, reviews, and feedback forms? Try a demo using your data</p>
                <Link to="/register" className="btn__try">Register Now</Link>
                <p className='home__ps'>Used by thousands of professional companies for business decisions</p>
            </div>
            {/* <img src="/assets/dashboard.png" alt="dashboard" /> */}
        </div>
    );
};

export default HomePage;