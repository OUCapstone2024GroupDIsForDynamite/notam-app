import React from "react";
import "../styles/NotamDetailCard.css"; 

const NotamDetailCard = ({ notam, onClose }) => {
  if (!notam) return null; // If no NOTAM is selected, don't display the card

  return (
    <div className="notam-detail-overlay" onClick={onClose}>
      <div className="notam-detail-card" onClick={(e) => e.stopPropagation()}>
        <h2>NOTAM ID: {notam.id}</h2>
        <div>
        {notam.affected_fir && <p><strong>Affected FIR:</strong> {notam.affected_fir}</p>}
        {notam.classification && <p><strong>Classification:</strong> {notam.classification}</p>}
        <p><strong>Effective Start:</strong> {new Date(notam.effective_start).toUTCString() || "N/A"}</p>
        <p><strong>Effective End:</strong> {new Date(notam.effective_end).toUTCString() || "N/A"}</p>
        {notam.location && <p><strong>Location:</strong> {notam.location}</p>}
        {notam.maximum_fl && <p><strong>Maximum FL:</strong> {notam.maximum_fl}</p>}
        {notam.minimum_fl && <p><strong>Minimum FL:</strong> {notam.minimum_fl}</p>}
        <div>
        {notam.purpose && (<p><strong>Purpose:</strong> {renderPurpose(notam.purpose)}</p>)}
        {notam.scope && (<p><strong>Scope:</strong> {scopeMap[notam.scope] || notam.scope}</p>)}
        {notam.traffic && (<p><strong>Traffic:</strong> {trafficMap[notam.traffic] || notam.traffic}</p>)}
        {notam.type && (<p><strong>Type:</strong> {typeMap[notam.type] || notam.type}</p>)}
    </div>
        <button onClick={onClose}>Close</button>
    </div>
    </div>
     {/* Add a new section for the full NOTAM text */}
     {notam.text && (
          <div className="notam-full-text">
            <h3>Full NOTAM Text</h3>
            <pre>{notam.text}</pre>
          </div>
        )}
    </div>
  );
  
};
const purposeMap = {
  "O": "Operational",
  "M": "Military",
  "A": "Administrative",
  "S": "Safety",
  "N": "Aircraft Operators",
  "B": "Brefing"
};  
// purpose can have combinations of letters, so we need to account for that
const renderPurpose = (purposeCode) => {
  if (!purposeCode) return null;

  // Split the string into an array of individual characters and map each to its description
  return purposeCode.split('').map((code, index) => (
    <span key={index}>{purposeMap[code] || code}</span>
  )).reduce((prev, curr) => [prev, ", ", curr]); // commas between multiple purposes
};

const scopeMap = {
  "I": "International",
  "D": "Domestic",
  "L": "Local",
  "G": "Global",
  "A": "Areodrome",
};

const trafficMap = {
  "V": "VFR (Visual Flight Rules)",
  "I": "IFR (Instrument Flight Rules)",
  "IV": "Both VFR and IFR",
  "X": "Not applicable to flight",
};

const typeMap = {
  "N": "Notice",
  "R": "Regulation",
  "A": "Advisory",
  "C": "Caution",
  "T": "Temporary",
};

export default NotamDetailCard;
