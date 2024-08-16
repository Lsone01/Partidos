# app1/urls.py

from django.urls import path
from .views import PartidoPoliticoListCreate, PartidoPoliticoRetrieveUpdateDestroy

urlpatterns = [
    path('partidos/', PartidoPoliticoListCreate.as_view(), name='partido-list-create'),
    path('partidos/<int:pk>/', PartidoPoliticoRetrieveUpdateDestroy.as_view(), name='partido-detail'),
]

