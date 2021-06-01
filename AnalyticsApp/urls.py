"""AnalyticsApp URL Configuration

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
from django.urls import path, include, re_path

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Using Django default authentication system
    path('', include('django.contrib.auth.urls')),
    # Call home.html from templates folder
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('state_listings', TemplateView.as_view(template_name='state_listings.html'), name='state_listings'),
    path('county_hotness',TemplateView.as_view(template_name = 'county_hotness.html'),name = 'county_hotness'),
    path('metro_hotness',TemplateView.as_view(template_name = 'metro_hotness.html'),name = 'metro_hotness'),
    path('zip_hotness',TemplateView.as_view(template_name = 'zip_hotness.html'),name = 'zip_hotness'),
    path('weekly_national',TemplateView.as_view(template_name = 'weekly_national.html'),name = 'weekly_national'),
]

