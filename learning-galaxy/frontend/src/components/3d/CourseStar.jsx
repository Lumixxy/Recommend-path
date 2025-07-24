import { Text } from '@react-three/drei';
import { motion } from 'framer-motion'; // Note the '3d' import

function CourseStar({ node, isCompleted, isUnlocked, onNodeClick }) {
  // Determine colors based on state
  const color = isCompleted ? "gold" : isUnlocked ? "royalblue" : "#333";
  const emissiveColor = isCompleted ? "gold" : isUnlocked ? "royalblue" : "black";

  return (
    <motion.group
      key={node.id}
      position={[node.position_x, node.position_y, node.position_z]}
      // Add hover effect only if unlocked
      whileHover={isUnlocked ? { scale: 1.2 } : { scale: 1 }}
      // Pass the click event up if unlocked
      onPointerDown={() => isUnlocked && onNodeClick(node.id)}
      animate={{ scale: isUnlocked ? 1 : 0.8 }} // Animate unlocked nodes
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
        visible={isUnlocked || isCompleted} // Only show text for visible nodes
      >
        {node.title}
      </Text>
    </motion.group>
  );
}

export default CourseStar;