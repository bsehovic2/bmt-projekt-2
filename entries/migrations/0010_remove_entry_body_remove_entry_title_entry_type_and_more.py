# Generated by Django 4.1.3 on 2023-01-15 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0009_rename_author_entry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='body',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='title',
        ),
        migrations.AddField(
            model_name='entry',
            name='type',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
    ]