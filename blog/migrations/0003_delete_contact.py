# Generated by Django 4.2 on 2024-08-08 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_contact_post_author_post_counted_view_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]