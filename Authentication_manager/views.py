from django.shortcuts import render,get_object_or_404
from .models import Profile
from allauth.account.views import SignupView


# Create your views here.


class Signup_View(SignupView):
    template_name = 'account/signup.html'


def home(request):
    return render(request, 'base.html')


def profile_view(request, username):
    # Retrieve the profile by filtering on the related user's username
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile/profile.html', {'profile': profile})
