from django.urls import path
from .views import Signup_View, home ,profile_view

urlpatterns = [
    path('signup/', Signup_View.as_view(), name='account-signup'),
    path('', home, name='home'),
    path('profile/<str:username>/', profile_view, name='profile')
]
