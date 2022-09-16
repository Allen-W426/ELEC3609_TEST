from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from requests import request

from users.models import Profile
from .models import ChatRoom
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)  # Import list view for class based view


class ChatDetailView(DetailView):
    model = ChatRoom


class SelfChatListView(ListView):
    model = ChatRoom
    template_name = "chat/user_chats.html"  # <app>/<model>_<view_type>.html
    context_object_name = 'user_chats'
    paginate_by = 5  # Paginate the chat to be 5, users will only view top 5 chats

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        query_set = ChatRoom.objects.filter(Q(buyer=user) | Q(seller_invited=user))
        return query_set

    def get_context_data(self, **kwargs):
        context = super(SelfChatListView, self).get_context_data(**kwargs)
        context['user'] = User.objects.filter(username=self.request.user.username)
        # Add any other variables to the context here
        user = get_object_or_404(User, username=self.request.user.username)
        context['user_chats'] = ChatRoom.objects.filter(Q(buyer=user) | Q(seller_invited=user))
        return context
