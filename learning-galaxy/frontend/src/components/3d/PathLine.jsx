import { Line } from '@react-three/drei';

function PathLine({ start, end }) {
  return (
    <Line
      points={[start, end]} // The start and end 3D coordinates
      color="skyblue"
      lineWidth={2}
    />
  );
}

export default PathLine;