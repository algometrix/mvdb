from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movie', views.MovieViewSet)
router.register(r'cast', views.CastViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'link', views.LinkViewSet)
