import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from '../api';
import LoadingIndicator from '../components/LoadingIndicator';

function Dashboard() {
    const [statistics, setStatistics] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        fetchStatistics();
    }, []);

    const fetchStatistics = async () => {
        try {
            const response = await api.get('/api/company/statistics/');
            setStatistics(response.data);
        } catch (error) {
            console.error('Failed to fetch statistics:', error);
            setError('Failed to load company statistics. Please try again later.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Dashboard</h1>
            <p>Welcome to your dashboard. Here's a quick overview:</p>
            <ul>
                <li><Link to="/company">View Company Information</Link></li>
                <li><Link to="/">Manage Your Notes</Link></li>
            </ul>

            <h2>Company Statistics</h2>
            {loading ? (
                <LoadingIndicator />
            ) : error ? (
                <p className="error">{error}</p>
            ) : statistics.length === 0 ? (
                <p>No statistics found for your company.</p>
            ) : (
                <ul>
                    {statistics.map((stat, index) => (
                        <li key={index}>{stat.name}: {stat.value}</li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default Dashboard;