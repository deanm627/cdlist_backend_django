from .models import CD
from rest_framework import viewsets
from .serializers import CDSerializer

# Create your views here.
class CDViewSet(viewsets.ModelViewSet):
    queryset = CD.objects.all()
    serializer_class = CDSerializer 