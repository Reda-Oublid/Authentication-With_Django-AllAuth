from django.urls import path
from .views import  home ,profile_view

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:username>/', profile_view, name='profile')
]
