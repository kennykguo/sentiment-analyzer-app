import './navigationItem.scss'; // Importing styles
import { Link } from "react-router-dom"; // Importing Link component for navigation

const NavigationItem = ({ children, to }) => {
    return (
        <li className='navigation__item'>
            <Link to={to}>{children}</Link>
        </li>
    );
};

export default NavigationItem;
