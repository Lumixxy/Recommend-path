from rest_framework import viewsets
from .models import CourseNode
from .serializers import CourseNodeSerializer

class CourseNodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list and retrieve actions.
    It returns all course nodes.
    """
    queryset = CourseNode.objects.all()
    serializer_class = CourseNodeSerializer