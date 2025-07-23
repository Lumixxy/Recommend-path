import React, { useState, useEffect } from 'react';
import { fetchCourses } from './services/api';
import Scene from './components/3d/Scene';
import './index.css'; // Make sure you have some basic CSS

function App() {
  const [courses, setCourses] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchCourses()
      .then(data => setCourses(data))
      .catch(err => setError(err.message));
  }, []);

  if (error) return <div className="message">Error: {error}</div>;
  if (!courses) return <div className="message">Loading Galaxy...</div>;

  return <Scene courses={courses} />;
}

export default App;