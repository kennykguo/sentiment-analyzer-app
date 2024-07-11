import { Outlet } from "react-router-dom"; // Importing Outlet for nested routes
import Header from "./Components/Header/Header"; // Importing Header component
import Footer from "./Components/Footer/Footer"; // Importing Footer component
import ModalWindow from "./Components/ModalLogForm/ModalLogForm"; // Importing ModalWindow component

const Layout = () => {
    return (
        <div className="wrapper">
            <div className="header">
                <Header />
            </div>
            <div className="content">
                <Outlet /> 
            </div>
            <div className="footer">
                <Footer />
            </div>
            <ModalWindow />
        </div>
    );
};

export default Layout;
