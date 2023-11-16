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


def get_user_profile_by_id(pk: int):
    try:
        user = CustomUser.objects.get(pk=pk)
        return user
    except CustomUser.DoesNotExist:
        return None  # User not found


def get_user_object(request):
    from server.users.models import CustomUser
    username = request.user.username
    try:
        user = CustomUser.objects.filter(username=username, is_deleted=False).first()
        if user is None:
            raise CustomUser.DoesNotExist
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


def confirm_email_by_token(request, token):
    try:
        user = get_user_object(request)
        if user.confirmation_token != token:
            return

        # Mark email as confirmed
        user.is_email_confirmed = True
        user.confirmation_token = None  # Clear the confirmation token
        user.save()
        return user
    except CustomUser.DoesNotExist:
        return None
