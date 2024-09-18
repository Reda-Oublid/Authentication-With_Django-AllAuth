from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from allauth.account.views import SignupView


# Create your views here.

@login_required
def home(request):
    return render(request, 'base.html')


@login_required
def profile_view(request, username):
    # Retrieve the profile by filtering on the related user's username
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile/profile.html', {'profile': profile})


@login_required
def profile_edit(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        profile.birthdate = request.POST.get('birthdate')
        profile.phone_number = request.POST.get('phone_number')
        profile.country = request.POST.get('country')
        profile.save()
        user.save()
        # this one returns you to the info page without need for refreshing
        return redirect('profile', username=username)
    else:
        return render(request, 'profile/profile.html', {'profile': profile})
