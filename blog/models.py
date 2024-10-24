from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from taggit.managers import TaggableManager
import sys

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
    category = models.ManyToManyField(Category, related_name='posts')
    tag = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    counted_view = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default='P', choices=STATUS_CHOICES)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)  # when the object first created,set current date and time
    update_date = models.DateTimeField(auto_now=True)  # when the object updated, save current date and time

    def save(self):  # this method resized all image
        im = Image.open(self.img)  # Opening the uploaded image
        output = BytesIO()
        im = im.resize((700, 353))  # Resize/modify the image
        im.save(output, format='JPEG', quality=100)  # after modifications, save it to the output
        output.seek(0)
        # change the imagefield value to be the newly modified image value
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Post, self).save()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return '{}'.format(self.title)

    # define an url for post based on id
    def get_absolute_url(self):
        return reverse('blog:single-blog', kwargs={'pid': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.email
