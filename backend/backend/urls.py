"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include, re_path
from profileapi import views as profile_views
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

class FrontendAppView(TemplateView):
    template_name = 'index.html'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profileapi.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Catch-all URL to serve the React app's index.html. This must come LAST.
urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
handler404 = profile_views.custom_404
handler500 = profile_views.custom_500
