from server.users.models import CustomUser


def get_user(*, pk: int = None, username: str = None, email: str = None) -> CustomUser | None:
    """
    Retrieve a CustomUser from the database using the provided parameters.

    :param pk: The primary key of the user.
    :param username: The username of the user.
    :param email: The email address of the user.
    :return: The CustomUser instance if found, otherwise None.
    """

    try:
        if pk:
            user = CustomUser.objects.get(pk=pk)
        elif username:
            user = CustomUser.objects.get(username=username)
        elif email:
            user = CustomUser.objects.get(email=email)
        else:
            """No parameters provided"""
            return None

        return user
    except CustomUser.DoesNotExist:
        """User not found"""
        return None


def get_user_profile_by_id(pk: int):
    """
    Retrieve a UserProfile from the database by user ID.

    :param pk: The primary key of the user.
    :return: The UserProfile instance if found, otherwise None.
    """

    try:
        user = CustomUser.objects.get(pk=pk)
        return user
    except CustomUser.DoesNotExist:
        """User not found"""
        return None


def check_if_user_exists(request):
    """
    Check if a user exists in the database.

    :param request: The request containing user data.
    :return: The CustomUser instance if found and not deleted, otherwise None.
    """

    from server.users.models import CustomUser
    username = request.data['username']
    try:
        user = CustomUser.objects.filter(username__exact=username, is_deleted=False).first()
        if user is None:
            raise CustomUser.DoesNotExist
        return user
    except CustomUser.DoesNotExist:
        return None


def get_user_object(request):
    """
    Retrieve a CustomUser from the database based on the request user.

    :param request: The request object.
    :return: The CustomUser instance if found and not deleted, otherwise None.
    """

    from server.users.models import CustomUser
    username = request.user.username
    try:
        user = CustomUser.objects.filter(username__exact=username, is_deleted=False).first()
        if user is None:
            raise CustomUser.DoesNotExist
        return user
    except CustomUser.DoesNotExist:
        return None


def get_user_profile(request):
    """
    Retrieve a UserProfile from the database based on the request user.

    :param request: The request object.
    :return: The UserProfile instance if found, otherwise None.
    """

    from server.users.models import UserProfile
    user = get_user_object(request)
    try:
        user_profile = UserProfile.objects.get(user=user)
        return user_profile
    except UserProfile.DoesNotExist:
        return None


def confirm_email_by_token(request, token):
    """
    Confirm the user's email by comparing the provided token.

    :param request: The request object.
    :param token: The confirmation token.
    :return: The CustomUser instance if the email is confirmed, otherwise None.
    """

    try:
        user = get_user_object(request)
        if user.confirmation_token != token:
            return

        """Mark email as confirmed"""
        user.is_email_confirmed = True
        """Clear the confirmation token field"""
        user.confirmation_token = None
        user.save()
        return user
    except CustomUser.DoesNotExist:
        return None
