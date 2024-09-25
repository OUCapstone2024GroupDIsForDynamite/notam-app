// pages/LandingPage.js
import React from "react";
import NotamCard from "../components/NotamCard"; // Import NotamCard component
import "../styles/LandingPage.css"; // Import CSS for styling

const LandingPage = () => {
  return (
    <div className="landing-page">
      <div>
        <h1>Welcome to the Landing Page</h1>
        <NotamCard />
      </div>
    </div>
  );
};

export default LandingPage;
