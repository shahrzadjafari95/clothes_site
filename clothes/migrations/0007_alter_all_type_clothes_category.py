# Generated by Django 4.2 on 2024-08-11 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0006_alter_all_type_clothes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_type_clothes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.category'),
        ),
    ]
