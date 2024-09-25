// App.js will render AppRoutes component to display pages depending on URL route.
import React from "react";
import AppRoutes from "./routes/AppRoutes"; // Import the Routes component

function App() {
  return (
    <div>
      <AppRoutes />
    </div>
  );
}

export default App;
