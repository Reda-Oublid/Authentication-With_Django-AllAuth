# Generated by Django 5.1 on 2024-09-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication_manager', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
