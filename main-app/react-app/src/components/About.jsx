// About.jsx

import React from 'react';
import '../styles/styles.css'; // Import the CSS file

function About() {
  return (
    <div className="about-container">
      <h1 className="about-header">About Us</h1>
      <p className="about-paragraph">
        Welcome to our application! Our mission is to provide users with the best experience possible. We are dedicated to continuous improvement and always looking for ways to enhance our services.
      </p>
      <p className="about-paragraph">
        Our team is made up of passionate individuals who are experts in their fields. We believe in the power of technology to transform lives and are committed to using it to make a positive impact on the world.
      </p>
      <p className="about-paragraph">
        Thank you for using our application. We hope you find it valuable and enjoyable. If you have any feedback or suggestions, please do not hesitate to reach out to us.
      </p>
    </div>
  );
}

export default About;