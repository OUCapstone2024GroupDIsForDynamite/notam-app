import React, { useState } from "react";
import "../styles/NotamCard.css"; // Import the CSS file for styling

const NotamCard = () => {
  const [notamNumber, setNotamNumber] = useState("");
  const [notam, setNotam] = useState(null);
  const [expanded, setExpanded] = useState(false);
  const [error, setError] = useState(""); // Added state for error message

  const handleInputChange = (e) => {
    setNotamNumber(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent form from submitting the default way
    setError(""); // Clear previous errors
    try {
      const response = await fetch(
        `http://localhost:5555/api/notam/${notamNumber}`
      );
      if (response.ok) {
        const data = await response.json();
        setNotam(data);
      } else {
        // Display error with dynamic status code and message
        const errorMessage = `Error ${response.status}: ${response.statusText}`;
        setNotam(null);
        setError(errorMessage);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setError("An error occurred while fetching the NOTAM."); // Set error message for any fetch errors
    }
  };

  const toggleExpand = () => {
    setExpanded(!expanded);
  };

  return (
    <div className="notam-card-container">
      <div
        className={`notam-card ${expanded ? "expanded" : ""}`}
        onClick={toggleExpand}
      >
        {error ? (
          <div className="notam-error">{error}</div> // Display error message inside the card
        ) : notam ? (
          expanded ? (
            <div className="notam-content">
              <h1 className="notam-heading">NOTAM {notam.number}</h1>
              <p>Series: {notam.series}</p>
              <p>ID: {notam.id}</p>
              <p>Description: {notam.description}</p>
              <p>Details: {notam.details}</p>
            </div>
          ) : (
            <h1 className="notam-heading">NOTAM {notam.number}</h1>
          )
        ) : (
          !error && (
            <h1 className="notam-heading">
              Enter a NOTAM number and fetch details
            </h1>
          )
        )}
      </div>
      <form onSubmit={handleSubmit} className="notam-form">
        <input
          type="text"
          value={notamNumber}
          onChange={handleInputChange}
          placeholder="Enter NOTAM number"
          className="notam-input"
        />
        <button type="submit" className="notam-submit-button">
          Fetch NOTAM
        </button>
      </form>
    </div>
  );
};

export default NotamCard;
