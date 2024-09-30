from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

gender_clothes = [('male', 'male'),
                  ('female', 'female'),
                  ('sport', 'sport')]

status = [('available', 'available'),
          ('finished', 'finished'),
          ('under production', 'under production')]


class Category(models.Model):
    name_category = models.CharField(max_length=255)

    def __str__(self):
        return self.name_category


class All_Type_Clothes(models.Model):
    image = models.ImageField(upload_to='clothes/')
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    price = models.FloatField()
    gender = models.CharField(max_length=255, choices=gender_clothes, default='male')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True)
    status = models.CharField(max_length=20, default='draft', choices=status)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def save(self):  # this method resized all image
        im = Image.open(self.image)  # Opening the uploaded image
        output = BytesIO()
        im = im.resize((230, 300))  # Resize/modify the image
        im.save(output, format='JPEG', quality=100)  # after modifications, save it to the output
        output.seek(0)
        # change the imagefield value to be the newly modified image value
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(All_Type_Clothes, self).save()

    def __str__(self):
        return self.gender

    class Meta:
        ordering = ['-created_date']


class Contact(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
