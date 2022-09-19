from django.urls import path
from . import views
from .views import (PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    DetailPost)

urlpatterns = [

    path('', PostListView.as_view(), name='blog_home'),
    path('about/', views.about, name='blog_about'),

    # Create post html pages for detail posts, which paths are specified by their post primary keys
    path('post/<int:pk>/', DetailPost.as_view(), name='post_detail'),

    # Create html page for a post creation form
    path('post/new/', PostCreateView.as_view(), name='post_create'),

    # Create post html pages for updating posts, which paths are specified by their post primary keys
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),

    # Create post html pages for deleting posts, which paths are specified by their post primary keys
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Create html for viewing user's personal posts specified by username
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
]
