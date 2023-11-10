from django.urls import path, include

from server.users.views import user_details

urlpatterns = [
    path('', user_details, name='user_details'),
    path('books/', include('server.books.urls'))
]
