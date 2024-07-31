import React, { useState, useEffect, useContext } from 'react';
import { AppContext } from '../Context';
import axios from 'axios';

// This component fetches and displays a list of companies.
// It uses the useContext hook to get the authentication token from AppContext.
// The useEffect hook is used to fetch companies when the component mounts or when the token changes.
// Axios is used to make the HTTP GET request to the backend API.
// The fetched companies are stored in the component's state using the useState hook.
// The companies are then rendered as a list in the JSX.

const CompanyPage = () => {
    const [companies, setCompanies] = useState([]);
    const { token } = useContext(AppContext);

    useEffect(() => {
        const fetchCompanies = async () => {
            try {
                const response = await axios.get('/api/companies/', {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setCompanies(response.data);
            } catch (error) {
                console.error('Error fetching companies:', error);
            }
        };
        fetchCompanies();
    }, [token]);

    return (
        <div className="company-list">
            <h1>Companies</h1>
            <ul>
                {companies.map(company => (
                    <li key={company.id} className="company-item">{company.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default CompanyPage;