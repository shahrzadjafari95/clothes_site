"""
URL configuration for clothes_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include, re_path
from . import views
from blog.sitemaps import BlogSitemap
from clothes.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}

# Define handler404 and handler500 for redirecting to maintenance
if settings.MAINTENANCE_MODE:
    handler404 = 'clothes_site.views.maintenance_view'
    handler500 = 'clothes_site.views.maintenance_view'  # handle 500 errors during maintenance

urlpatterns = []


if settings.MAINTENANCE_MODE:
    # Redirect all traffic to the maintenance view
    urlpatterns += [
        re_path(r'^.*$', views.maintenance_view),  # Catch-all URL
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('django.contrib.auth.urls')),
        path('', include('clothes.urls')),
        path('blog/', include('blog.urls')),
        path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
        path('robots.txt', include('robots.urls')),
        path("__debug__/", include("debug_toolbar.urls")),
        path('summernote/', include('django_summernote.urls')),
        path('captcha/', include('captcha.urls')),  # captcha urls
        path('accounts/', include('accounts.urls')),
    ]
    # Add static and media files handling
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
