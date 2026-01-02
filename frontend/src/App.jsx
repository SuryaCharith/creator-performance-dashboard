import "./App.css";
import { useEffect, useState } from "react";
import { fetchAnalytics, fetchMetrics } from "./api";

function App() {
  const [platform, setPlatform] = useState("");
  const [metrics, setMetrics] = useState(null);
  const [rows, setRows] = useState([]);

  useEffect(() => {
    fetchMetrics(platform).then(setMetrics);
    fetchAnalytics(platform).then(setRows);
  }, [platform]);

  return (
    <div className="app-container">

      <h1>Creator Performance Dashboard</h1>

      <select onChange={(e) => setPlatform(e.target.value)}>
        <option value="">All Platforms</option>
        <option value="instagram">Instagram</option>
        <option value="youtube">YouTube</option>
      </select>

      {metrics && (
        <div className="metrics">
  <div className="metric-card">
    Impressions <br /> {metrics.total_impressions}
  </div>
  <div className="metric-card">
    Engagement <br /> {metrics.total_engagement}
  </div>
  <div className="metric-card">
    Followers Gained <br /> {metrics.followers_gained}
  </div>
</div>

      )}

      <table border="1" cellPadding="8" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th>Platform</th>
            <th>Date</th>
            <th>Impressions</th>
            <th>Likes</th>
            <th>Comments</th>
            <th>Followers</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id}>
              <td>{r.platform}</td>
              <td>{r.date}</td>
              <td>{r.impressions}</td>
              <td>{r.likes}</td>
              <td>{r.comments}</td>
              <td>{r.followers_gained}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
