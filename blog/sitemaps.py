from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):  # The items() method determines what data or objects will be included in the sitemap.

        # This method queries the Post model to get all posts where the status is "A" and published_date less than now
        return Post.objects.filter(status="A", published_date__lte=timezone.now())

    def location(self, item):  # This method defines the URL for each item (blog post) returned by the items() method.

        # The location() method generates the URL for each of those posts using their primary key (item.pk).
        return reverse('blog:single-blog', kwargs={'pid': item.pk})
