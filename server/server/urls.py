from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from server.views import HomeView, UserRegistrationView, UserLogoutView, UserLoginView, MyBooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('', HomeView.as_view(), name='home'),
    path('my-books/', MyBooksView.as_view(), name='my-books'),
    path('users/', include('server.users.urls')),
    path('books/', include('server.books.urls')),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
