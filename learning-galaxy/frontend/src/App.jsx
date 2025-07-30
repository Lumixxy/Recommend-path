import React, { useState, useEffect } from 'react';
import Scene from './components/3d/Scene';
import CourseDetailsModal from './components/ui/CourseDetailsModal';
import { fetchCourses } from './services/api';
import './index.css';
import { demoSheet } from './theatre';

function App() {
  const [courses, setCourses] = useState(null);
  const [error, setError] = useState(null);
  const [completedCourses, setCompletedCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);

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

  const handleNodeClick = (course) => {
    // Get a reference to the camera object at the moment of the click
    const cameraSheetObject = demoSheet.object('Camera');

    // Tell Theatre.js to animate the camera to the new position
    cameraSheetObject.setValues({
      position: { x: course.position_x, y: course.position_y, z: course.position_z + 10 },
    });

    // Play a short sequence to trigger the animation
    demoSheet.sequence.play({ duration: 1.5 }).then(() => {
      // Open the modal AFTER the animation finishes
      setSelectedCourse(course);
    });
  };

  const handleCourseComplete = (courseId) => {
    setCompletedCourses(prev => prev.includes(courseId) ? prev : [...prev, courseId]);
  };

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