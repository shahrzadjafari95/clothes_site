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
