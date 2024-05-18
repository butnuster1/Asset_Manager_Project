"""
Asset_Manager_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from Asset_Manager_App.views import AssetList, AssetDetail, AssetAdd
from django.urls import include, re_path
import Asset_Manager_App.views


urlpatterns = [
    #Uncomment the next line to enable the admin:
    
    # path('', AssetList.as_view(), name='assets'),
    path('asset/<int:pk>/', AssetDetail.as_view(), name='asset'),
    path('asset-create/', AssetAdd.as_view(), name='asset-create'),
    path('admin/', admin.site.urls),
    re_path(r'^$', Asset_Manager_App.views.index, name='index'),
    re_path(r'^home$', Asset_Manager_App.views.index, name='home'),
    re_path(r'^schedule$', Asset_Manager_App.views.schedule, name='schedule'),
]
