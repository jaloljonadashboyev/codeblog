# Generated by Django 3.2.13 on 2022-05-05 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_post_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
    ]