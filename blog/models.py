from PIL import Image
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
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

    def save(self, *args, **kwargs):
        try:
            # Check if an instance already exists to handle old image deletion
            old_instance = Post.objects.get(pk=self.pk)
            if old_instance.img and old_instance.img != self.img:
                old_instance.img.delete(save=False)
        except Post.DoesNotExist:
            # Instance doesn't exist; this is a new object
            pass

        # Resize image only if it's a new upload
        if self.img and not default_storage.exists(self.img.name):
            im = Image.open(self.img)
            output = BytesIO()

            # Convert image mode to RGB if necessary
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")

            # Resize the image
            im = im.resize((700, 353))
            im.save(output, format='JPEG', quality=85)
            output.seek(0)

            # Replace the image with the resized one
            self.img = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.img.name.split('.')[0]}.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None
            )

        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

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


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
