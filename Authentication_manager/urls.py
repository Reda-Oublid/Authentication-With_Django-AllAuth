from django.urls import path
from .views import home, profile_view, profile_edit

urlpatterns = [
    path('', home, name='home'),
    path('profile/<str:username>/', profile_view, name='profile'),
    # path for profile edit view here
    path('profile/<str:username>/edit/', profile_edit, name='profile_edit'),
]
