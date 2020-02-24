from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import redirect_blog
from django.contrib import admin


urlpatterns = [
	path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('pars/', include('pars.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)