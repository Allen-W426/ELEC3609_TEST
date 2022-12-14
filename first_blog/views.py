from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from .models import Post  # From the models.py import Post table
from chat.models import ChatRoom
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView, DetailView)  # Import list view for class based view


# Create your views here.


def home(request):
    context = {
        'fake_Post': Post.objects.all()
    }
    return render(request, 'first_blog/blog_home.html', context)


def about(request):
    return render(request, 'first_blog/blog_about.html', {'title': 'blog_about'})


# Create a class inherent from list view
class PostListView(ListView):
    model = Post
    template_name = "first_blog/blog_home.html"  # <app>/<model>_<view_type>.html
    context_object_name = 'fake_Post'
    ordering = ['-date_posted']  # Ordering post from latest to oldest
    paginate_by = 5  # Paginate the post to be 5, users will only view top 5 posts


# Create a class inherent from list view, only to load post for current user
class UserPostListView(ListView):
    model = Post
    template_name = "first_blog/user_posts.html"  # <app>/<model>_<view_type>.html
    context_object_name = 'fake_Post'
    ordering = ['-date_posted']  # Ordering post from latest to oldest
    paginate_by = 5  # Paginate the post to be 5, users will only view top 5 posts

    # Method for viewing current user's personal post, filtered by author name
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class DetailPost(View):

    def get(self, request, pk):
        context = {"object": Post.objects.get(id=pk)}
        # add the dictionary during initialization

        return render(request, "first_blog/post_detail.html", context)

    def post(self, request, pk):
        new_chat_room = ChatRoom.objects.create(buyer=self.request.user, seller_invited=Post.objects.get(id=pk).author)
        new_chat_room.save()

        return HttpResponseRedirect(reverse('chatroom_detail', kwargs={'pk': new_chat_room.pk}))


# Create a class inherent from create view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Create a function specify the post author to the user
    # sending post request when creating the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Create a class inherent from update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Create a function specify the post author to the user
    # sending post request when updating the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Only allow user to update own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Create a class inherent from delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # Direct user to home page after deletion
    success_url = '/'

    # Only allow user to delete own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


