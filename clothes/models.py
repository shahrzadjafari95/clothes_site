from io import BytesIO
import sys
from PIL import Image
from django.core.files.storage import default_storage
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

    def save(self, *args, **kwargs):
        # Handle deletion of the old image
        if self.pk:  # Only check for old instance if this is an update
            try:
                old_instance = All_Type_Clothes.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except All_Type_Clothes.DoesNotExist:
                pass

        # Resize image only if it's a new upload or updated image
        if self.image and hasattr(self.image, 'file'):
            try:
                im = Image.open(self.image.file)
                output = BytesIO()

                # Convert image to RGB if necessary
                if im.mode in ("RGBA", "P"):
                    im = im.convert("RGB")

                # Resize the image to the desired dimensions
                im = im.resize((230, 300))
                im.save(output, format='JPEG', quality=85)
                output.seek(0)

                # Replace the image with the resized one
                self.image = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f"{self.image.name.split('.')[0]}.jpg",
                    'image/jpeg',
                    sys.getsizeof(output),
                    None
                )
            except Exception as e:
                print(f"Error processing image: {e}")  # Log the error

        # Call the parent class's save method
        super(All_Type_Clothes, self).save(*args, **kwargs)

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

    class Meta:
        ordering = ['-created_date']
