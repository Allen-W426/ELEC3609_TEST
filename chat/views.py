from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http.response import JsonResponse, HttpResponse

from .models import ChatRoom, Message
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)  # Import list view for class based view


def ChatDetailView(request, pk):
    user = request.user
    current_room = ChatRoom.objects.get(id=pk)
    return render(request, 'chat/chatroom_detail.html', {
        'user': user,
        'current_room': current_room,
    })


def CreateMsgInstance(request):
    chatroomID = request.POST['chatroomID']
    msg_content = request.POST['msg_content']
    user = request.POST['user']
    chatroom = ChatRoom.objects.filter(id=chatroomID)[0]

    new_message = Message.objects.create(msg_content=msg_content, msg_writer=request.user,
                                         chatRoomID=chatroom)
    new_message.save()
    return HttpResponse('Message sent successfully')


def GetCurrentRoomMsgs(request, pk):
    cur_room = ChatRoom.objects.get(id=pk)
    messages = Message.objects.filter(chatRoomID=cur_room.id)

    return JsonResponse({"messages": list(messages.values())})


class SelfChatListView(ListView):
    model = ChatRoom
    template_name = "chat/user_chats.html"  # <app>/<model>_<view_type>.html
    context_object_name = 'user_chats'
    paginate_by = 5  # Paginate the chat to be 5, users will only view top 5 chats

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        query_set = ChatRoom.objects.filter(Q(buyer=user) | Q(seller_invited=user))
        return query_set

    def get_context_data(self, **kwargs):
        context = super(SelfChatListView, self).get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, username=self.kwargs.get('username'))
        # Add any other variables to the context here
        user = get_object_or_404(User, username=self.request.user.username)
        context['user_chats'] = ChatRoom.objects.filter(Q(buyer=user) | Q(seller_invited=user))
        return context
