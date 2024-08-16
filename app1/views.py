from rest_framework import generics
from .models import PartidoPolitico
from .serializers import PartidoPoliticoSerializer

class PartidoPoliticoListCreate(generics.ListCreateAPIView):
    queryset = PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer

class PartidoPoliticoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer
