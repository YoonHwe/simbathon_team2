# Generated by Django 3.2.4 on 2021-06-23 01:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0024_cave_post_nolaw_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='nolaw_Post',
            new_name='action_Post',
        ),
    ]