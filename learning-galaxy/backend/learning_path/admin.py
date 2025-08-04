from django.contrib import admin
from .models import Role, CourseNode, UserProgress

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(CourseNode)
class CourseNodeAdmin(admin.ModelAdmin):
    list_display = ['title', 'role', 'parent', 'position_x', 'position_y', 'position_z']
    list_filter = ['role', 'parent']
    search_fields = ['title', 'description']
    filter_horizontal = ['prerequisites']
    raw_id_fields = ['parent']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'content', 'course_url')
        }),
        ('Relationships', {
            'fields': ('role', 'parent', 'prerequisites')
        }),
        ('3D Positioning', {
            'fields': ('position_x', 'position_y', 'position_z')
        }),
    )

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'completed_courses_count']
    search_fields = ['user__username']
    filter_horizontal = ['completed_courses']
    
    def completed_courses_count(self, obj):
        return obj.completed_courses.count()
    completed_courses_count.short_description = 'Completed Courses'