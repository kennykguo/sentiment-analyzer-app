import './homePage.scss'; // Importing HomePage styles

const HomePage = () => {
    return (
        <div className='home__container'>
            <div className="home__context">
                <h1 className='home__title'>AI-Powered<br/> Customer Feedback<br/> Analytics</h1>
                <p className='home__descr'>Want to understand what your customers say in support calls, reviews, and feedback forms? Try a Lumoa demo using your data.</p>
                <button className="btn__try">Try it</button>
                <p className='home__ps'>Trusted by thousands CX leaders</p>
            </div>
            <img src="../../assets/dashboard.png" alt="dashboard" />
        </div>
    );
};

export default HomePage;
