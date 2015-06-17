from rest_framework import serializers
from storage.models import Movie, Cast, Genre, Link

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cast
        fields=('id','name')
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=('id','name')
        
class LinkSerializer(serializers.ModelSerializer):
    #movie = serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all(), allow_null=True)
    class Meta:
        model=Link
        fields=('id','url','movie')
        
class MovieSerializer(serializers.ModelSerializer):
    link = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Movie
        fields=('id','name','cast','link','genre','rating','screenshot_1','screenshot_2','cover_image','size_mb',)


        
