from rest_framework import viewsets, permissions
# Import the authentication classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication 
from .models import Role, CourseNode, UserProgress
from .serializers import RoleSerializer, CourseNodeSerializer, UserProgressSerializer

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset provides read-only access to roles.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view roles

class CourseNodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list and retrieve actions.
    It returns all course nodes.
    """
    queryset = CourseNode.objects.all()
    serializer_class = CourseNodeSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view courses

class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    # Add this line to specify which authentication methods to use
    authentication_classes = [SessionAuthentication, TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        # Return only the progress for the current logged-in user
        return UserProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the progress with the logged-in user
        serializer.save(user=self.request.user)