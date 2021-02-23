from django.urls import path

from . import views


urlpatterns = [
    path('movie/', views.MoviesListView.as_view()),
    path('movie/<int:pk>/', views.MoviesDetailView.as_view()),
    path('review/', views.ReviewCreateView.as_view()),
    path('rating/', views.AddStarRatingView.as_view()),

]