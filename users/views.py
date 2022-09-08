from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Import UserRegistrationForm, User Update Form, Profile Update Form methods
# from the same folder in forms.py
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # If request is post, which indicate user wants to update the account
    if request.method == 'POST':
        # Rename functions, and specify the instance of the user information who wants to update the form
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        # If both user update form and profile update form is valid, save these forms
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # Display success msg after updates
            messages.success(request, f'Your account  has been updated.')

            # Redirect to url named profile page after successful registration
            # profile name is specified in project main file/urls.py
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
