from rest_framework import viewsets
from rest_framework import permissions

from .serializers import QuerySerializer
from .models import BigQuery


class Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BigQuery.objects.all()
    serializer_class = QuerySerializer


