"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from portfolio.views import home, project_detail
from django.conf import settings
from django.conf.urls.static import static
from blog.views import blog_index, blog_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('project/<slug:slug>/', project_detail, name='project_detail'),
    path('', include('portfolio.urls')),
    path('blog/', blog_index, name='blog_index'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)