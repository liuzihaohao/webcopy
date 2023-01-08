"""webcopy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from django.views.static import serve
from . import settings
from message.views import messgaelistdbViewSet,settingslistdbViewSet,indexhome,seachdb,fileup,uptext

router = routers.DefaultRouter()
router.register(r'v1/message', messgaelistdbViewSet)
router.register(r'v1/settingslist', settingslistdbViewSet)

urlpatterns = [
    path('',indexhome),
    path('seachdb/',seachdb),
    path('uptext/',uptext),
    path('upfile/',fileup),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    # path("media/<path>",down),
]
