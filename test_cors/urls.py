"""test_cors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


@api_view(http_method_names=['GET'])
@renderer_classes([JSONRenderer])
def ping(request):
    return Response({
        'message': 'successful',
        'success': True,
    })

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ping/$', ping),
]
