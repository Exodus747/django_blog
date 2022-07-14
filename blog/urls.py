from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SelfPostListView
)
from . import views
from .views import  AddCommentView

urlpatterns = [
    path('', views.home, name='landing'),
    path('main/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('selff/<str:username>', SelfPostListView.as_view(), name='self-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search_user, name='search-user'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),


]
