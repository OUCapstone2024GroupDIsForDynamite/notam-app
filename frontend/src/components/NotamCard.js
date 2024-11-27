import React, { useState } from "react";
import "../styles/NotamCard.css";
import NotamDetailCard from "./NotamDetailCard"; 

const NotamCard = () => {
  const [departureLocation, setDepartureLocation] = useState("");
  const [arrivalLocation, setArrivalLocation] = useState("");
  const [notams, setNotams] = useState(null);
  const [error, setError] = useState("");
const [selectedNotam, setSelectedNotam] = useState(null);
const handleRowClick = (notam) => setSelectedNotam(notam);
// default columns
  const [visibleColumns, setVisibleColumns] = useState([
    "location",
    "issued",
    "id",
    "text",
    "type",
    "effective_start",
    "effective_end",
    "traffic",
  ]);

  const [showColumnDropdown, setShowColumnDropdown] = useState(false);

  const handleDepartureChange = (e) => {
    setDepartureLocation(e.target.value);
  };

  const handleArrivalChange = (e) => {
    setArrivalLocation(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const response = await fetch(
        `http://localhost:5555/api/notam/${departureLocation}/${arrivalLocation}`
      );
      console.log(response);
      if (response.ok) {
        const data = await response.json();
        console.log("Fetched NOTAM data:", data); // log fetched data
        setNotams(data);
      } else {
        // Display error with dynamic status code and message
        const errorMessage = `Error ${response.status}: ${response.statusText}`;
        console.log(
          `Error fetching NOTAM for location ${location}: Status ${response.status}`
        );
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
      setError("An error occurred while fetching the NOTAM.");
    }
  };

  const handleCheckboxChange = (e) => {
    const { value, checked } = e.target;
    setVisibleColumns((prevColumns) => {
      if (checked) {
        return [...prevColumns, value];
      } else {
        return prevColumns.filter((col) => col !== value);
      }
    });
  };

  return (
    <div className="notam-content">
      <div className="input-container">
        <input
          type="text"
          value={departureLocation}
          onChange={handleDepartureChange}
          placeholder="Enter Departure Airport Code"
          className="notam-input"
        />
        <input
          type="text"
          value={arrivalLocation}
          onChange={handleArrivalChange}
          placeholder="Enter Arrival Airport Code"
          className="notam-input"
        />
        <button type="submit" className="notam-submit-button" onClick={handleSubmit}>
          Fetch NOTAMS
        </button>
        <div style={{ position: "relative" }}>
          <button
            className="dropdown-toggle"
            onClick={() => setShowColumnDropdown(!showColumnDropdown)}
          >
            Customize Columns &#x25BC;
          </button>
  
          {showColumnDropdown && (
            <div className="dropdown-menu">
              {[
                "account_id",
                "affected_fir",
                "classification",
                "effective_start",
                "effective_end",
                "icao_location",
                "id",
                "issued",
                "last_updated",
                "location",
                "maximum_fl",
                "minimum_fl",
                "number",
                "purpose",
                "scope",
                "selection_code",
                "series",
                "text",
                "traffic",
                "type",
              ].map((col) => (
                <div key={col} className="dropdown-item">
                  <input
                    type="checkbox"
                    value={col}
                    checked={visibleColumns.includes(col)}
                    onChange={handleCheckboxChange}
                  />
                  <label>{col.replace(/_/g, " ")}</label>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
  
      {error && <div className="notam-error">{error}</div>}
      {notams && notams.length > 0 && (
        <>
          <h1>NOTAM Data</h1>
          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  {visibleColumns.includes("account_id") && <th>Account ID</th>}
                  {visibleColumns.includes("affected_fir") && <th>Affected FIR</th>}
                  {visibleColumns.includes("classification") && <th>Classification</th>}
                  {visibleColumns.includes("effective_start") && <th>Effective Start</th>}
                  {visibleColumns.includes("effective_end") && <th>Effective End</th>}
                  {visibleColumns.includes("icao_location") && <th>ICAO Location</th>}
                  {visibleColumns.includes("id") && <th>ID</th>}
                  {visibleColumns.includes("issued") && <th>Issued</th>}
                  {visibleColumns.includes("last_updated") && <th>Last Updated</th>}
                  {visibleColumns.includes("location") && <th>Location</th>}
                  {visibleColumns.includes("maximum_fl") && <th>Maximum FL</th>}
                  {visibleColumns.includes("minimum_fl") && <th>Minimum FL</th>}
                  {visibleColumns.includes("number") && <th>Number</th>}
                  {visibleColumns.includes("purpose") && <th>Purpose</th>}
                  {visibleColumns.includes("scope") && <th>Scope</th>}
                  {visibleColumns.includes("selection_code") && <th>Selection Code</th>}
                  {visibleColumns.includes("series") && <th>Series</th>}
                  {visibleColumns.includes("text") && <th>Text</th>}
                  {visibleColumns.includes("traffic") && <th>Traffic</th>}
                  {visibleColumns.includes("type") && <th>Type</th>}
                </tr>
              </thead>
              <tbody>
                {notams.map((item, index) => (
                  <tr key={index} onClick={() => handleRowClick(item)}>
                    {visibleColumns.includes("account_id") && <td>{item.account_id}</td>}
                    {visibleColumns.includes("affected_fir") && <td>{item.affected_fir}</td>}
                    {visibleColumns.includes("classification") && <td>{item.classification}</td>}
                    {visibleColumns.includes("effective_start") && (
                      <td>{new Date(item.effective_start).toLocaleDateString()}</td>
                    )}
                    {visibleColumns.includes("effective_end") && (
                      <td>{new Date(item.effective_end).toLocaleDateString()}</td>
                    )}
                    {visibleColumns.includes("icao_location") && <td>{item.icao_location}</td>}
                    {visibleColumns.includes("id") && <td>{item.id}</td>}
                    {visibleColumns.includes("issued") && (
                      <td>{new Date(item.issued).toLocaleDateString()}</td>
                    )}
                    {visibleColumns.includes("last_updated") && (
                      <td>{new Date(item.last_updated).toLocaleDateString()}</td>
                    )}
                    {visibleColumns.includes("location") && <td>{item.location}</td>}
                    {visibleColumns.includes("maximum_fl") && <td>{item.maximum_fl}</td>}
                    {visibleColumns.includes("minimum_fl") && <td>{item.minimum_fl}</td>}
                    {visibleColumns.includes("number") && <td>{item.number}</td>}
                    {visibleColumns.includes("purpose") && <td>{item.purpose}</td>}
                    {visibleColumns.includes("scope") && <td>{item.scope}</td>}
                    {visibleColumns.includes("selection_code") && <td>{item.selection_code}</td>}
                    {visibleColumns.includes("series") && <td>{item.series}</td>}
                    {visibleColumns.includes("text") && (
                      <td className="text-column">{item.text}</td>
                    )}
                    {visibleColumns.includes("traffic") && <td>{item.traffic}</td>}
                    {visibleColumns.includes("type") && <td>{item.type}</td>}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
  
      {/* Render NotamDetailCard if a NOTAM is selected */}
      {selectedNotam && (
        <NotamDetailCard notam={selectedNotam} onClose={() => setSelectedNotam(null)} />
      )}
    </div>
  );  
};

export default NotamCard;
