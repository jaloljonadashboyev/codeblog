from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', DetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article', HomeView.as_view(), name='article'),
    path('article/<int:pk>/update', UpdatePostView.as_view(), name='update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path("like/<int:pk>/", LikeView, name="like_post"),
]