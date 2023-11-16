from django.urls import path

from server.users.views import user_details, confirm_email, UserProfileUpdateAPIView, UserProfileDeleteView

urlpatterns = [
    path('', user_details, name='user_details'),
    path('confirm-email/<str:token>/', confirm_email, name='confirm_email'),
    path('update-profile/', UserProfileUpdateAPIView.as_view(), name='update_user_profile'),
    path('delete/', UserProfileDeleteView.as_view(), name='delete_user')
]
