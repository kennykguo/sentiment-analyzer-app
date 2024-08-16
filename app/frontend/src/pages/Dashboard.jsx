import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from '../api';
import LoadingIndicator from '../components/LoadingIndicator';
import '../index.css';

function Dashboard() {
    const [statistics, setStatistics] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        fetchStatistics();
    }, []);

    const fetchStatistics = async () => {
        try {
            const response = await api.get('/api/statistics/');
            console.log('Fetched response data:', response.data);
            setStatistics(response.data);
        } catch (error) {
            console.error('Failed to fetch statistics:', error);
            setError('Failed to load company statistics. Please try again later.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-[#EEEEEE] flex flex-col items-center justify-center p-8">
            <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-4xl">
                <img src="src/assets/logo.jpg" alt="Logo" className="h-12 mb-6 mx-auto" />
                <h1 className="text-3xl font-bold text-center text-[#201E43] mb-6">Dashboard</h1>
                <p className="text-center mb-6">Welcome to your dashboard. Here's a quick overview:</p>
                <div className="flex justify-center space-x-4 mb-8">
                    <Link to="/company" className="bg-[#134B70] text-white py-2 px-4 rounded-md hover:bg-[#508C9B] transition duration-300 ease-in-out">
                        View Company Information
                    </Link>
                </div>

                <h2 className="text-2xl font-bold text-center text-[#201E43] mb-4">Company Statistics</h2>
                {loading ? (
                    <LoadingIndicator />
                ) : error ? (
                    <p className="text-red-500 text-center">{error}</p>
                ) : statistics.length === 0 ? (
                    <p className="text-center">No statistics found for your company.</p>
                ) : (
                    <ul className="space-y-2">
                        {statistics.map((stat, index) => (
                            <li key={index} className="flex flex-col bg-gray-100 p-3 rounded">
                                <p className="font-semibold">Review: {stat.review}</p>
                                <p>VADER Score: {stat.vader_score}</p>
                                <p>Prediction: {stat.model_prediction}</p>
                                <p>Avg. Sentiment Score: {stat.avg_sentiment_score}</p>
                                <p>Avg. Word Count: {stat.avg_word_count}</p>
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
}

export default Dashboard;
