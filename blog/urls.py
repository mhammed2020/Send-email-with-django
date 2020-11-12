from django.urls import path
from .views import (
    PostListView,
    # PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ProjectListView
    
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('project/', ProjectListView.as_view(), name='allPosts'),

        path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

        path('detail/<int:post_id>/', views.post_detail, name='post-detail'),

    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('project/',views.allProjects,name='allPosts'),


    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]