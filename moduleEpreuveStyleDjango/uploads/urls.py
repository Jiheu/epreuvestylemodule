from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from uploads.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^classement/$', views.classement, name='classement'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
