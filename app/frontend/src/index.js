import React from 'react'; // Importing React
import ReactDOM from 'react-dom/client'; // Importing ReactDOM for rendering
import App from './App'; // Importing main App component
import 'bootstrap/dist/css/bootstrap.min.css'; // Importing Bootstrap CSS
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Importing Bootstrap JS
import { BrowserRouter } from 'react-router-dom'; // Importing BrowserRouter for routing
import Context from './Context'; // Importing Context provider

const root = ReactDOM.createRoot(document.getElementById('root')); // Creating a root to render the app
root.render(
    <React.StrictMode>
        <Context>
            <BrowserRouter>
                <App />
            </BrowserRouter>
        </Context>
    </React.StrictMode>
);
