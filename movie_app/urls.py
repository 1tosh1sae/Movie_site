from django.urls import path, include
from rest_framework import routers
from .views import (RegisterView, LogoutView, LoginView, UserProfileDetailAPiView, UserProfileListAPIView, CategoryListSerializer,
CategoryDetailAPIView, CountryListAPIView,CountryDetailAPIView,
DirectorListAPiView, DirectorDetailAPIView, ActorListAPIView, ActorDetailAPIView, GenreListAPiView, MovieListAPIView,MovieDetailAPIView,
 ReviewViewSet, RatingViewSet,ReviewLikeViewSet, FavoriteViewSet,
FavoriteMovieViewSet, HistoryViewSet, CategoryListAPIview,GenreDetailAPiView)


router = routers.DefaultRouter()
router.register('ratings', RatingViewSet)
router.register('reviews', ReviewViewSet)
router.register('review-likes', ReviewLikeViewSet)
router.register('favorites', FavoriteViewSet)
router.register('history', HistoryViewSet)
router.register('favorite-movies', FavoriteMovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPiView.as_view(), name='user_detail'),
    path('category/', CategoryListAPIview.as_view(),name= 'category_list'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name= 'category_detail'),
    path('genre/', GenreListAPiView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPiView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movies_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movies_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPiView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
]