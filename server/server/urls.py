from django.contrib import admin
from django.urls import path, include

from server.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('users/', include('server.users.urls')),
    path('books/', include('server.books.urls'))
]
