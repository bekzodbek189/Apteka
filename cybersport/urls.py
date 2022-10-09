from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import *
from api.views_b import *
from api import urls_a, urls_b

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tablet_create/", Tablet_create),
    path("", include(urls_a)),
    path('add_product/', ADD)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)