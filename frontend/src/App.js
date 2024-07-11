import './app.scss'; // Importing app styles
import { Route, Routes } from "react-router-dom"; // Importing routing components
import Layout from "./Layout"; // Importing Layout component
import HomePage from './Components/HomePage/HomePage'; // Importing HomePage component

function App() {
    return (
        <>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<HomePage />} />
                </Route>
            </Routes>
        </>
    );
}

export default App;
