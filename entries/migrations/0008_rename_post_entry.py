# Generated by Django 4.1.3 on 2022-12-19 16:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0007_delete_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Entry',
        ),
    ]
