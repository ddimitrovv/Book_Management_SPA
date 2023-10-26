from django.shortcuts import get_object_or_404


def get_user_object(request):
    from server.users.models import CustomUser
    username = request.user
    return get_object_or_404(CustomUser, username=username)


def get_user_profile(request):
    from server.users.models import UserProfile
    user = get_user_object(request)
    return get_object_or_404(UserProfile, user=user)
