# Generated by Django 4.1.3 on 2022-12-08 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_rename_comment_comment_body_comment_date_posted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]