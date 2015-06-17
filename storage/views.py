from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie, Cast, Genre, Link
from .serializers import MovieSerializer, CastSerializer, GenreSerializer, LinkSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.order_by('id')
    serializer_class = MovieSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (permissions.IsAuthenticated(),)
    
class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.order_by('id')
    serializer_class = CastSerializer
    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.order_by('id')
    serializer_class = GenreSerializer
    
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.order_by('id')
    serializer_class = LinkSerializer