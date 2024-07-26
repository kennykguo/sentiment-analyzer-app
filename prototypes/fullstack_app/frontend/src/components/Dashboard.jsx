import React, { useContext, useEffect, useState } from 'react';
import { AppContext } from '../Context';
import axios from 'axios';

const Dashboard = () => {
    const { user, token } = useContext(AppContext);
    const [statistics, setStatistics] = useState(null);

    useEffect(() => {
        const fetchStatistics = async () => {
            try {
                const response = await axios.get('/api/statistics/', {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setStatistics(response.data);
            } catch (error) {
                console.error('Error fetching statistics:', error);
            }
        };

        fetchStatistics();
    }, [token]);

    return (
        <div className="dashboard">
            <h1>Welcome to your Dashboard, {user.name}!</h1>
            {statistics && (
                <div className="dashboard-stats">
                    <h2>Your Statistics</h2>
                    <p>Total Sentiments: {statistics.total_sentiments}</p>
                    <p>Positive Sentiments: {statistics.positive_sentiments}</p>
                    <p>Negative Sentiments: {statistics.negative_sentiments}</p>
                </div>
            )}
        </div>
    );
};

export default Dashboard;