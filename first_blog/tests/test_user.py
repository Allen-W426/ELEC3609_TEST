from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from first_blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User
from users.forms import UserRegisterForm, UserUpdateForm
from first_blog.views import PostCreateView


class TestUserAuth(TestCase):

    # Set up function to initialize the client
    def setUp(self):
        self.username = 'test_username'
        self.password = 'testing12345'
        self.user = User.objects.create(username=self.username)
        self.user.set_password(self.password)
        self.user.save()

        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')

    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEquals(response.status_code, 302)

    def test_register_get(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)

    def test_register_post_success(self):
        response = self.client.post(self.register_url, {
            'username': 'test_user2',
            'password1': 'testing323rtq',
            'password2': 'testing323rtq',
            'email': 'wrar@uni.sydney.edu.au',
        })
        self.assertEquals(response.status_code, 302)

    def test_register_post_fail_email_invalid(self):
        response = self.client.post(self.register_url, {
            'username': 'test_user2',
            'password1': 'testing323rtq',
            'password2': 'testing323rtq',
            'email': 'wrar@gmail.com',
        })
        self.assertEquals(response.status_code, 200)

    def test_register_post_fail_password_short(self):
        response = self.client.post(self.register_url, {
            'username': 'test_user2',
            'password1': '4dig',
            'password2': '4dig',
            'email': 'wrar@uni.sydney.edu.au',
        })
        self.assertEquals(response.status_code, 200)

    def test_register_post_fail_password_confirm_diff(self):
        response = self.client.post(self.register_url, {
            'username': 'test_user2',
            'password1': 'only7digwqewq',
            'password2': 'only7digwefwef',
            'email': 'wrar@uni.sydney.edu.au',
        })
        self.assertEquals(response.status_code, 200)

    def test_user_registration_form_valid(self):
        form = UserRegisterForm(data={
            'username': 'test_user2',
            'password1': 'testing323rtq',
            'password2': 'testing323rtq',
            'email': 'wrar@uni.sydney.edu.au',
        })
        self.assertTrue(form.is_valid())

    def test_profile_form_success(self):
        form = UserUpdateForm(data={
            'username': 'test_user2',
            'email': 'wrar@uni.sydney.edu.au',
        })
        self.assertTrue(form.is_valid())

    def test_profile_form_fail_email_invalid(self):
        form = UserUpdateForm(data={
            'username': 'test_user2',
            'email': 'wrar@gmail.com',
        })
        self.assertFalse(form.is_valid())

    def test_create_profile_model(self):
        self.test_profile = self.user.profile
        self.assertEquals(str(self.test_profile), 'test_username Profile')

 
