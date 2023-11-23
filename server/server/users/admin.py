from django.contrib import admin

from server.users.models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CustomUser model.

    Attributes:
    - list_display (list): Fields to display in the list view.
    - search_fields (list): Fields to use in the admin search.
    """

    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username']
    search_help_text = 'Search for user by username'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.

    Attributes:
    - list_display (list): Fields to display in the list view.
    - search_fields (list): Fields to use in the admin search.
    """

    list_display = ['first_name', 'last_name', 'gender', 'user']
    search_fields = ['user__username']
    search_help_text = 'Search for user profile by username'
