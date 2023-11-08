from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from server.books.operations import get_all_books_by_user
from server.books.serializers import BookSerializer
from server.users.operations import get_user_profile
from server.users.serializers import CustomUserSerializer, UserProfileSerializer


@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = get_user_profile(request)
        books = get_all_books_by_user(user=user)
    else:
        user = None
        user_profile = None
        books = None

    user_data = CustomUserSerializer(user).data if user else None
    user_profile_data = UserProfileSerializer(user_profile).data if user_profile else None
    books_data = {book.pk: BookSerializer(book).data for book in books} if books else None

    data = {
        'user': user_data,
        'user_profile': user_profile_data,
        'books': books_data,
    }

    return JsonResponse(data)
