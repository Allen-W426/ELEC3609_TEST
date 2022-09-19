from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import (ChatDetailView,
                    SelfChatListView)

urlpatterns = [
    path('chat/<int:pk>/', ChatDetailView.as_view(), name='chatroom_detail'),

    path('chat/<str:username>/', SelfChatListView.as_view(), name='user_chat'),
]
