from django.urls import path

from server.users.views import UserDetails, confirm_email, UserProfileUpdateAPIView, UserProfileDeleteView

urlpatterns = [
    path('', UserDetails.as_view(), name='user_details'),
    path('confirm-email/<str:token>/', confirm_email, name='confirm_email'),
    path('update-profile/', UserProfileUpdateAPIView.as_view(), name='update_user_profile'),
    path('delete/', UserProfileDeleteView.as_view(), name='delete_user')
]
