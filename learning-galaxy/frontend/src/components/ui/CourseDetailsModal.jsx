import React from 'react';

function CourseDetailsModal({ course, onClose, onComplete, isCompleted }) {
  if (!course) return null;

  const handleCompleteClick = () => {
    onComplete(course.id);
    onClose(); // Close the modal after completing
  };

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <h2>{course.title}</h2>
        <p>{course.description}</p>
        
        <div className="modal-buttons">
          <button onClick={onClose}>Close</button>
          <button 
            onClick={handleCompleteClick}
            disabled={isCompleted}
            className={isCompleted ? 'completed-btn' : ''}
          >
            {isCompleted ? 'Completed' : 'Complete Course'}
          </button>
        </div>

      </div>
    </div>
  );
}

export default CourseDetailsModal;