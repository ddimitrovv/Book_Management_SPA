from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
