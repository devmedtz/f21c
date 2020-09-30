from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('super-admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('main.urls', namespace='main')),
    path('admin/', include('admins.urls', namespace='admins')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)