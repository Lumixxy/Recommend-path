import { Text } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import { val } from '@theatre/core';
import { editable, PerspectiveCamera } from '@theatre/r3f';
import { useRef } from 'react';

function CourseStar({ node, isCompleted, isUnlocked, onNodeClick }) {
  const color = isCompleted ? "gold" : isUnlocked ? "royalblue" : "#333";
  const emissiveColor = isCompleted ? "gold" : isUnlocked ? "royalblue" : "black";
  const starRef = useRef();

  // This is a simplified animation, Theatre.js can do much more complex sequences
  useFrame(({ camera }) => {
    // A subtle floating animation can be added here if desired
  });

  return (
    <group 
      ref={starRef}
      key={node.id}
      position={[node.position_x, node.position_y, node.position_z]}
      onPointerDown={() => isUnlocked && onNodeClick(node)}
    >
      <mesh>
        <sphereGeometry args={[1.5, 32, 32]} />
        <meshStandardMaterial 
          color={color} 
          emissive={emissiveColor} 
          emissiveIntensity={0.5} 
          roughness={0.4}
        />
      </mesh>
      <Text
        position={[0, 2.5, 0]}
        fontSize={1.2}
        color="white"
        anchorX="center"
        anchorY="middle"
        visible={isUnlocked || isCompleted}
      >
        {node.title}
      </Text>
    </group>
  );
}

export default CourseStar;