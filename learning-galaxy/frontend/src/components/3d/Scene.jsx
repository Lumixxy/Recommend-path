import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stars } from '@react-three/drei';

function Scene({ courses }) {
  return (
    <Canvas camera={{ position: [0, 0, 50], fov: 75 }}>
      {/* Lighting and environment */}
      <ambientLight intensity={0.5} />
      <Stars />
      
      {/* Render a sphere for each course */}
      {courses.map(course => (
        <mesh 
          key={course.id} 
          position={[course.position_x, course.position_y, course.position_z]}
        >
          <sphereGeometry args={[1.5, 32, 32]} />
          <meshStandardMaterial color="royalblue" />
        </mesh>
      ))}

      {/* Camera controls */}
      <OrbitControls />
    </Canvas>
  );
}

export default Scene;