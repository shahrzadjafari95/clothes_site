from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    # This method returns a list of URL names (defined in your urls.py) that should be included in the sitemap.
    def items(self):
        return ["clothes:home_page", "clothes:men-clothes", "clothes:women-clothes", "clothes:contact"]

    # The reverse(item) function uses this item to retrieve the actual URL associated with that URL name from your urls.
    def location(self, item):
        return reverse(item)  # item is one of the values from the list returned by items()
