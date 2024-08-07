import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    const [isVisible, setIsVisible] = useState(false);

    useEffect(() => {
        const timer = setTimeout(() => {
            setIsVisible(true);
        }, 500);

        return () => clearTimeout(timer);
    }, []);

    return (
        <div className="min-h-screen bg-gradient-to-br from-[#201E43] to-[#134B70] text-white">
            <div className={`container mx-auto px-4 py-16 transition-opacity duration-1000 ${isVisible ? 'opacity-100' : 'opacity-0'}`}>
                <h1 className="text-5xl font-bold mb-8 text-center animate-fadeIn">Welcome to ML4U</h1>
                <p className="text-xl mb-12 text-center animate-fadeIn animation-delay-200">Revolutionizing businesses through AI and Machine Learning</p>
                
                <div className="grid md:grid-cols-2 gap-12 mb-16">
                    <div className="bg-white bg-opacity-10 p-8 rounded-lg animate-fadeIn animation-delay-400">
                        <h2 className="text-2xl font-semibold mb-4">Our Expertise</h2>
                        <ul className="list-disc list-inside space-y-2">
                            <li>Text Analysis: Uncover customer sentiments</li>
                            <li>Predictive Analytics: Forecast trends and behaviors</li>
                            <li>Computer Vision: Automate visual data processing</li>
                            <li>Natural Language Processing: Enhance communication systems</li>
                        </ul>
                    </div>
                    <div className="bg-white bg-opacity-10 p-8 rounded-lg animate-fadeIn animation-delay-600">
                        <h2 className="text-2xl font-semibold mb-4">Why Choose ML4U?</h2>
                        <ul className="list-disc list-inside space-y-2">
                            <li>Cutting-edge machine learning solutions</li>
                            <li>Customized AI-driven strategies</li>
                            <li>Expert consultancy and hands-on project support</li>
                            <li>Proven track record across various industries</li>
                        </ul>
                    </div>
                </div>
                
                <p className="text-center text-xl mb-8 animate-fadeIn animation-delay-800">
                    Ready to transform your data into actionable insights and unlock new possibilities for your business?
                </p>
                
                <div className="flex justify-center space-x-6 animate-fadeIn animation-delay-1000">
                    <Link to="/register" className="bg-[#508C9B] hover:bg-[#134B70] text-white font-bold py-3 px-6 rounded-full transition duration-300">
                        Get Started
                    </Link>
                    <Link to="/login" className="bg-transparent hover:bg-white hover:text-[#201E43] text-white font-bold py-3 px-6 rounded-full border-2 border-white transition duration-300">
                        Log In
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default Home;