export async function fetchCourses() {
    const response = await fetch('http://127.0.0.1:8000/api/courses/');
    if (!response.ok) {
      throw new Error('Failed to fetch course data from the API.');
    }
    return response.json();
  }