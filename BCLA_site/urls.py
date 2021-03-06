"""BCLA_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
import network.views as network_views

urlpatterns = [
    path('', network_views.home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('all/', network_views.return_all_node, name='all_node'),
    path('node/', include('network.urls')),
    path('description/', network_views.return_node_description, name='node_description'),
    path('download/', network_views.download_file, name='download_file')
]
