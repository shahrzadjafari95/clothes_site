from django.contrib.sitemaps import Sitemap
from django.utils import timezone

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):  # The items() method determines what data or objects will be included in the sitemap.

        # This method queries the Post model to get all posts where the status is "A" and published_date less than now
        return Post.objects.filter(status="A", published_date__lte=timezone.now())
