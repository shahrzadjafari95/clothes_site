from django.contrib import sitemaps
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    # This method returns a list of URL names (defined in your urls.py) that should be included in the sitemap.
    def items(self):
        return ["clothes:home_page", "clothes:men-clothes", "clothes:women-clothes", "clothes:contact"]
