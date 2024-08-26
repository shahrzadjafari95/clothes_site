from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
STATUS_CHOICES = (
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('R', 'Rejected'),
)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    counted_view = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default='P', choices=STATUS_CHOICES)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)  # when the object first created,set current date and time
    update_date = models.DateTimeField(auto_now=True)  # when the object updated, save current date and time

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return '{} {}'.format(self.title, self.pk)

    # define an url for post based on id
    def get_absolute_url(self):
        return reverse('blog:single-blog', kwargs={'pid': self.pk})
