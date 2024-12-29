import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:3000/get-soil-data")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
    <h1>Soil Moisture Data</h1>
    <ul>
        {data.map((entry) => (
            <li key={entry._id}>
                Value: {entry.moistureValue}, Timestamp: {new Date(entry.createdAt).toLocaleString()}
            </li>
        ))}
    </ul>
</div>

  );
}

export default App;
