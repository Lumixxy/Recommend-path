from rest_framework import viewsets, permissions
from .models import CourseNode, UserProgress
from .serializers import CourseNodeSerializer, UserProgressSerializer

class CourseNodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list and retrieve actions.
    It returns all course nodes.
    """
    queryset = CourseNode.objects.all()
    serializer_class = CourseNodeSerializer

class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged-in users can access

    def get_queryset(self):
        # Return only the progress for the current logged-in user
        return UserProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the progress with the logged-in user
        serializer.save(user=self.request.user)