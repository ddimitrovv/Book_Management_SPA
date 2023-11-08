from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from server.users.views import get_csrf_token, user_registration, user_login, user_logout

urlpatterns = [
    path('token/', get_csrf_token, name='get_csrf_token'),
    path('register/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]


# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
