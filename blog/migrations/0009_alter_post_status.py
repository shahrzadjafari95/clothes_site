# Generated by Django 4.2 on 2024-08-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_counted_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]
