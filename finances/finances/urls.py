from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('consumer/', include('consumer.urls'), name='consumer'),
    path('profile/', include('consumer_profile.urls'), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
