from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.name

class CourseNode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Each course can belong to one primary role, like "Backend" or "Frontend"
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    
    # This is the key field: It allows a course to require other courses as prerequisites
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    # 3D coordinates for the frontend to use
    position_x = models.FloatField(default=0)
    position_y = models.FloatField(default=0)
    position_z = models.FloatField(default=0)

    def _str_(self):
        return self.title