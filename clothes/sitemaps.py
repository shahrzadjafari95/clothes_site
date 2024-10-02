from django.contrib import sitemaps
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

