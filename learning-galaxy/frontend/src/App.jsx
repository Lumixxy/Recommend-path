import React, { useState, useEffect } from 'react';
import Scene from './components/3d/Scene';
import CourseDetailsModal from './components/ui/CourseDetailsModal';
import { fetchCourses } from './services/api';
import './index.css';

function App() {
  // State hooks
  const [courses, setCourses] = useState(null);
  const [error, setError] = useState(null);
  const [completedCourses, setCompletedCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);

  // Effect to fetch data on mount
  useEffect(() => {
    fetchCourses()
      .then(data => {
        setCourses(data);
        const startingNodeIds = data
          .filter(course => course.prerequisites.length === 0)
          .map(course => course.id);
        setCompletedCourses(startingNodeIds);
      })
      .catch(err => setError(err.message));
  }, []);

  // Handler for opening the modal
  const handleNodeClick = (courseId) => {
    const course = courses.find(c => c.id === courseId);
    setSelectedCourse(course);
  };

  // Handler for completing a course
  const handleCourseComplete = (courseId) => {
    setCompletedCourses(prev => prev.includes(courseId) ? prev : [...prev, courseId]);
  };

  // Render logic
  if (error) return <div className="message">Error: {error}</div>;
  if (!courses) return <div className="message">Loading Galaxy...</div>;

  return (
    <>
      <Scene 
        courses={courses} 
        completedCourses={completedCourses} 
        onNodeClick={handleNodeClick}
      />
      <CourseDetailsModal 
        course={selectedCourse} 
        onClose={() => setSelectedCourse(null)}
        onComplete={handleCourseComplete}
        isCompleted={selectedCourse && completedCourses.includes(selectedCourse.id)}
      />
    </>
  );
}

export default App;