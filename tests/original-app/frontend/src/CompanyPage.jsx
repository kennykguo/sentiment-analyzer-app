import React, { useState, useEffect } from 'react';
import axios from '../axios';

const CompanyPage = () => {
    const [companies, setCompanies] = useState([]);

    useEffect(() => {
        const fetchCompanies = async () => {
            const response = await axios.get('companies/');
            setCompanies(response.data);
        };
        fetchCompanies();
    }, []);

    return (
        <div>
            <h1>Companies</h1>
            <ul>
                {companies.map(company => (
                    <li key={company.id}>{company.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default CompanyPage;
