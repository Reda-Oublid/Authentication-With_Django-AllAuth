from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar', 'preferences', 'birthdate', 'phone_number', 'country')
    search_fields = ('user__username', 'bio', 'preferences', 'country')
    list_filter = ('preferences', 'birthdate', 'country')
    ordering = ('-birthdate',)
