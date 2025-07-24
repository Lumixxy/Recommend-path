import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stars, Text } from '@react-three/drei';
import PathLine from './PathLine';
import CourseStar from './CourseStar';

function Scene({ courses, completedCourses, onNodeClick }) {
  const courseMap = new Map(courses.map(course => [course.id, course]));

  const isUnlocked = (course) => {
    return course.prerequisites.every(prereqId => completedCourses.includes(prereqId));
  };

  return (
    <Canvas camera={{ position: [0, 5, 50], fov: 75 }}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <Stars />
      
      {courses.map(course => (
        <CourseStar
          key={course.id}
          node={course}
          isCompleted={completedCourses.includes(course.id)}
          isUnlocked={isUnlocked(course)}
          onNodeClick={onNodeClick}
        />
      ))}

      {courses.map(course => {
        if (!isUnlocked(course)) return null; 

        return course.prerequisites.map(prereqId => {
          const prereqNode = courseMap.get(prereqId);
          if (!prereqNode) return null;

          const startPoint = [prereqNode.position_x, prereqNode.position_y, prereqNode.position_z];
          const endPoint = [course.position_x, course.position_y, course.position_z];
          
          // The fix is in the 'key' prop below
          return <PathLine key={`${prereqId}-${course.id}`} start={startPoint} end={endPoint} />;
        });
      })}
      
      <OrbitControls />
    </Canvas>
  );
}

export default Scene;