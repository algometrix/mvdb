from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie, Cast, Genre, Link
from .serializers import MovieSerializer, CastSerializer, GenreSerializer, LinkSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.order_by('id')
    serializer_class = MovieSerializer
    
    def get_queryset(self):
        result=Movie.objects.all()
        movie_name=self.request.query_params.get('name',None)
        if movie_name:
            return result.filter(name__icontains=movie_name)
        
        return result
    
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (permissions.IsAuthenticated(),)
    
class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.order_by('id')
    serializer_class = CastSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (permissions.IsAuthenticated(),)
    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.order_by('id')
    serializer_class = GenreSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (permissions.IsAuthenticated(),)
    
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.order_by('id')
    serializer_class = LinkSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (permissions.IsAuthenticated(),)