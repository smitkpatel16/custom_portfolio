from django.urls import path
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio', views.portfolio, name='home2'),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
