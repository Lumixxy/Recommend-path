from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CourseNode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField(blank=True, help_text="Detailed course content in markdown format")
    course_url = models.URLField(blank=True, help_text="External link to the course")
    
    # Each course can belong to one primary role, like "Backend" or "Frontend"
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    
    # Parent-child relationships for hierarchical structure
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    
    # This is the key field: It allows a course to require other courses as prerequisites
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    # 3D coordinates for the frontend to use
    position_x = models.FloatField(default=0)
    position_y = models.FloatField(default=0)
    position_z = models.FloatField(default=0)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    # Link progress to a specific user. Each user can only have one progress entry.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Store the list of all courses the user has completed.
    completed_courses = models.ManyToManyField(CourseNode, blank=True)

    def __str__(self):
        return f"Progress for {self.user.username}"