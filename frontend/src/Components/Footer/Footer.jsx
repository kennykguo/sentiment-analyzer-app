import './footer.scss'; // Importing footer styles
import NavigationItem from "../NavigationItem/NavigationItem"; // Importing the NavigationItem component
import { AppContext } from '../../Context'; // Importing context for state management
import { useContext } from 'react'; // Importing useContext hook to use the context

const Footer = () => {
    const { handlerOpen } = useContext(AppContext); // Destructuring handlerOpen from context

    return (
        <>
            <div className="footer__main">
                <img className="footer__logo" src="../../assets/logo.jpg" alt="logo" />
                <p className="footer__copyright">Copyright | &copy;2022<br/>All rights reserved<br/>Web-development</p>
            </div>
            <ul className="footer__nav">
                <NavigationItem to='/'>Product</NavigationItem>
                <NavigationItem to='/analysis'>Customer Review Analysis</NavigationItem>
            </ul>
            <ul className="footer__nav">
                <NavigationItem to='/pricing'>Pricing</NavigationItem>
            </ul>
            <ul className="footer__nav">
                <NavigationItem to='/about'>About</NavigationItem>
                <NavigationItem to='/about/team'>Our team</NavigationItem>
            </ul>
            <ul className="footer__nav">
                <NavigationItem to=''>Get in touch</NavigationItem>
                <NavigationItem to=''>Support</NavigationItem>
                <NavigationItem to=''>
                    <button className="btn__login" onClick={handlerOpen}>Log in</button>
                </NavigationItem>
            </ul>
        </>
    );
};

export default Footer;
