from rest_framework import serializers
from .models import Role, CourseNode, UserProgress

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']

class CourseNodeSerializer(serializers.ModelSerializer):
    # 'role' will be represented by its string name from the Role model
    role = serializers.StringRelatedField()

    class Meta:
        model = CourseNode
        # We explicitly list all fields to be included in the API response
        fields = [
            'id', 
            'title', 
            'description', 
            'content',
            'course_url',
            'role', 
            'parent',
            'prerequisites', 
            'position_x', 
            'position_y', 
            'position_z'
        ]

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['completed_courses']