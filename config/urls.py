"""Main URLs module."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/v1/', include(('curso_api_rest.users.urls', 'users'), namespace='users'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)