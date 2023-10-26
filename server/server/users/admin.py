from django.contrib import admin

from server.users.models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username']
    search_help_text = 'Search for user by username'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'user']
    search_fields = ['user__username']
    search_help_text = 'Search for user profile by username'
