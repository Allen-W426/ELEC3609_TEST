"""project_start_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views  # Import views for creating user authentication
from django.urls import path, include
from users import views as user_views  # Import methods in views.py from users directory to urls
from django.conf import settings  # Import snippets for user uploading media files in media root
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Create an url for home page
    path('', include('first_blog.urls')),

    # Create an url for all paths in chat
    path('', include('chat.urls')),

    # Create an url for user registration
    path('register/', user_views.register, name='register'),

    # Create an url for user login with template from login.html in users folder
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Create an url for user logout with template from logout.html in users folder
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Create an url for user login with template from profile.html in users folder
    path('profile/', user_views.profile, name='profile'),

    ###
    # Create an url for user to reset password using email
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),

    # Create an url after users have reset passwords successfully
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    ###
]

# If your MEDIA_URL is defined as /media/,
# you can do this by adding the following snippet to your urls.py:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
