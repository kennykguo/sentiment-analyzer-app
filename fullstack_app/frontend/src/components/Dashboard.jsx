import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = ({ token }) => {
  const [companyData, setCompanyData] = useState(null);
  const [sentiments, setSentiments] = useState([]);
  const [statistics, setStatistics] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Set up axios with the authorization header
        const axiosInstance = axios.create({
          headers: { Authorization: `Bearer ${token}` }
        });

        // Fetch company data
        const companyResponse = await axiosInstance.get('http://localhost:8000/api/company/');
        setCompanyData(companyResponse.data);

        // Fetch sentiments
        const sentimentsResponse = await axiosInstance.get('http://localhost:8000/api/sentiments/');
        setSentiments(sentimentsResponse.data);

        // Fetch statistics
        const statisticsResponse = await axiosInstance.get('http://localhost:8000/api/statistics/');
        setStatistics(statisticsResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [token]);

  if (!companyData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Welcome, {companyData.name}!</h1>
      <h2>Sentiments:</h2>
      {sentiments.length === 0 ? (
        <p>No sentiments available.</p>
      ) : (
        <ul>
          {sentiments.map((sentiment) => (
            <li key={sentiment.id}>{sentiment.review}</li>
          ))}
        </ul>
      )}
      <h2>Statistics:</h2>
      {statistics ? (
        <div>
          <p>Mean: {statistics.mean}</p>
          <p>Standard Deviation: {statistics.standard_deviation}</p>
        </div>
      ) : (
        <p>No statistics available.</p>
      )}
    </div>
  );
};

export default Dashboard;
