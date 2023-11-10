from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from server.views import home_view, user_registration, user_logout, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', home_view, name='home'),
    path('<int:user_id>/', include('server.users.urls'))
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
