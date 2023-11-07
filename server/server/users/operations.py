from server.users.models import CustomUser


def get_user(*, pk: int = None, username: str = None, email: str = None) -> CustomUser | None:
    try:
        if pk:
            user = CustomUser.objects.get(pk=pk)
        elif username:
            user = CustomUser.objects.get(username=username)
        elif email:
            user = CustomUser.objects.get(email=email)
        else:
            return None  # No parameters provided

        return user
    except CustomUser.DoesNotExist:
        return None  # User not found


def get_user_object(request):
    from server.users.models import CustomUser
    username = request.user.username
    try:
        user = CustomUser.objects.get(username=username)
        return user
    except CustomUser.DoesNotExist:
        return None


def get_user_profile(request):
    from server.users.models import UserProfile
    user = get_user_object(request)
    try:
        user_profile = UserProfile.objects.get(user=user)
        return user_profile
    except UserProfile.DoesNotExist:
        return None
