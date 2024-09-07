import React, { useState, useEffect } from 'react';

function App() {
  const [state, setState] = useState({
    msg: ''
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5555/api/notams'); // Replace with your API endpoint
      const data = await response.json();

      // Assuming the API response contains variable1 and variable2
      setState({
        msg: data.msg
      });
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };



  return (
    <div>
      <h1>{state.msg}</h1>
    </div>

  );
}

export default App;
