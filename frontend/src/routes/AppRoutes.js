// routes/Routes.js
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LandingPage from "../pages/LandingPage"; // Only route for LandingPage

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} /> {/* Root route */}
      </Routes>
    </Router>
  );
};

export default AppRoutes;
