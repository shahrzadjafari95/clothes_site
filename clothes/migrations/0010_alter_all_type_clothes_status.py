# Generated by Django 4.2 on 2024-08-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0009_alter_all_type_clothes_options_alter_contact_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_type_clothes',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]
