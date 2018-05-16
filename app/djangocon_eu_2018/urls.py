"""djangocon_eu_2018 URL Configuration

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

from demo import views as demo_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'basic/$', demo_views.basic),
    url(r'links/$', demo_views.links),
    url(r'^$', demo_views.home, name='home'),
    url(r'search/$', demo_views.search, name='search'),
    url(r'search/(?P<link>\d+)$', demo_views.search, name='search-link'),
    url(r'detail/$', demo_views.detail, name='detail'),
    url(r'detail/(?P<link>\d+)$', demo_views.detail, name='detail-link'),
]
