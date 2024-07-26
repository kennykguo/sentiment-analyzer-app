import './header.scss'; // Importing header styles
import NavigationItem from '../NavigationItem/NavigationItem'; // Importing the NavigationItem component
import { AppContext } from '../../Context'; // Importing context for state management
import { useContext } from 'react'; // Importing useContext hook to use the context

const Header = () => {
    const { handlerOpen } = useContext(AppContext); // Destructuring handlerOpen from context
    
    return (
        <>
            <img className="header__logo" src="../assets/logo.jpg" alt="logo" />
            <ul className="navigation">
                <NavigationItem to='/'>Product <span>&#11167;</span></NavigationItem>
                <NavigationItem to='/pricing'>Pricing <span>&#11167;</span></NavigationItem>
                <NavigationItem to='/about'>About <span>&#11167;</span></NavigationItem>
            </ul>
            <div className="wrapp__buttons">
                <button className="btn__try">Try it</button>
                <button className="btn__login" onClick={handlerOpen}>Log in</button>
            </div>
        </>
    );
};

export default Header;
