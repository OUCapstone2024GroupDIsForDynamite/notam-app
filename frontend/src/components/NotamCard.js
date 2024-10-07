import React, { useState } from "react";
import "../styles/NotamCard.css"; // Import the CSS file for styling

const NotamCard = () => {
  const [departureLocation, setDepartureLocation] = useState("");
  const [arrivalLocation, setArrivalLocation] = useState("");
  const [notams, setNotams] = useState(null);
  const [expanded, setExpanded] = useState(false);
  const [error, setError] = useState(""); // Added state for error message

  const handleDepartureChange = (e) => {
    setDepartureLocation(e.target.value);
  };

  const handleArrivalChange = (e) => {
    setArrivalLocation(e.target.value);
  }

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent form from submitting the default way
    setError(""); // Clear previous errors
    try {
      const response = await fetch(
        `http://localhost:5555/api/notam/${departureLocation}/${arrivalLocation}`
      );
      console.log(response)
      if (response.ok) {
        const data = await response.json();
        console.log("Fetched NOTAM data:", data) // log fetched data
        setNotams(data);
      } else {
        // Display error with dynamic status code and message
        const errorMessage = `Error ${response.status}: ${response.statusText}`;
        console.log(`Error fetching NOTAM for location ${location}: Status ${response.status}`);
        setNotams(null);
        if (response.status === 404) {
          setError("NOTAM not found for the specified location.");
        } else if (response.status === 400) {
          setError("Invalid request. Please check the ICAO location code.");
        } else if (response.status === 500) {
          setError("Server error. Please try again later.");
        } else {
          setError("An unexpected error occurred. Please try again.");
        }
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
    <div className="notam-content">
    <div>
      <form onSubmit={handleSubmit} className="notam-form">
        <input
          type="text"
          value={departureLocation}
          onChange={handleDepartureChange}
          placeholder="Enter Departure Airport Code"
          className="notam-input"
        />
      </form>
      <form onSubmit={handleSubmit} className="notam-form">
        <input
          type="text"
          value={arrivalLocation}
          onChange={handleArrivalChange}
          placeholder="Enter Arrival Airport Code"
          className="notam-input"
        />
      </form>
      <form onSubmit={handleSubmit}>
        <button type="submit" className="notam-submit-button">
          Fetch NOTAM
        </button>
      </form>
    </div>
    {error ? (
          <div className="notam-error">{error}</div> // Display error message inside the card
    ) : notams && notams.length > 0 ? (
      <div>
      <div>
            <h1>NOTAM Data</h1>
            <table border="1" cellPadding="10" style={{ borderCollapse: 'collapse', width: '100%' }}>
                <thead>
                    <tr>
                        <th>Account ID</th>
                        <th>Affected FIR</th>
                        <th>Classification</th>
                        <th>Effective Start</th>
                        <th>Effective End</th>
                        <th>ICAO Location</th>
                        <th>ID</th>
                        <th>Issued</th>
                        <th>Last Updated</th>
                        <th>Location</th>
                        <th>Maximum FL</th>
                        <th>Minimum FL</th>
                        <th>Number</th>
                        <th>Purpose</th>
                        <th>Scope</th>
                        <th>Selection Code</th>
                        <th>Series</th>
                        {/* <th>Text</th> */}
                        <th>Traffic</th>
                        <th>Type</th>
                    </tr>
                </thead>
                <tbody>
                    {notams.map((item, index) => (
                        <tr key={index}>
                            <td>{item.accountId}</td>
                            <td>{item.affectedFIR}</td>
                            <td>{item.classification}</td>
                            <td>{new Date(item.effectiveStart).toLocaleDateString()}</td>
                            <td>{new Date(item.effectiveEnd).toLocaleDateString()}</td>
                            <td>{item.icaoLocation}</td>
                            <td>{item.id}</td>
                            <td>{new Date(item.issued).toLocaleDateString()}</td>
                            <td>{new Date(item.lastUpdated).toLocaleDateString()}</td>
                            <td>{item.location}</td>
                            <td>{item.maximumFL}</td>
                            <td>{item.minimumFL}</td>
                            <td>{item.number}</td>
                            <td>{item.purpose}</td>
                            <td>{item.scope}</td>
                            <td>{item.selectionCode}</td>
                            <td>{item.series}</td>
                            {/* <td>{item.text}</td> */}
                            <td>{item.traffic}</td>
                            <td>{item.type}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>      
    </div>
      ) :null }
    </div>
  );
};

export default NotamCard;
