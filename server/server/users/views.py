from django.http import HttpResponse

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from server.users.models import UserProfile
from server.users.operations import get_user_profile, confirm_email_by_token, get_user_object
from server.users.serializers import CustomUserSerializer, UserProfileSerializer, UserProfileUpdateSerializer


class UserDetails(APIView):

    def get(self, request, *args, **kwargs):
        user = get_user_object(request)
        if not user:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_authenticated:
            user_profile = get_user_profile(request)

            return Response(
                {
                    'user': CustomUserSerializer(user).data,
                    'user_profile': UserProfileSerializer(user_profile).data
                },
                status=status.HTTP_200_OK
            )


def confirm_email(request, token):
    user = confirm_email_by_token(request, token)
    if user:
        return HttpResponse('Email confirmed successfully!', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error', status=status.HTTP_404_NOT_FOUND)


class UserProfileUpdateAPIView(APIView):

    def patch(self, request, *args, **kwargs):

        user = get_user_object(request)

        if user.is_authenticated:
            user_profile = UserProfile.objects.get(user=user)
            serializer = UserProfileUpdateSerializer(user_profile, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response(
                    {
                        'user_profile': UserProfileSerializer(user_profile).data
                    },
                    status=status.HTTP_200_OK
                )
            return Response({'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDeleteView(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def delete(self, request, *args, **kwargs):
        user = get_user_object(request)
        user.is_deleted = True
        user.save()
        return Response({'detail': 'Profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
