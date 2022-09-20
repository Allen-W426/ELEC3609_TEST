from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import (ChatDetailView,
                    SelfChatListView)

urlpatterns = [
    path('chat/<int:pk>/',ChatDetailView, name='chatroom_detail'),

    path('chat/<str:username>/', SelfChatListView.as_view(), name='user_chat'),

    path('msg_creation/', views.CreateMsgInstance, name='msg_create'),

    path('getMessages/<int:pk>/', views.GetCurrentRoomMsgs, name='get_msgs'),

]
