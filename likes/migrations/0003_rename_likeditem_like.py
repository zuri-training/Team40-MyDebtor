# Generated by Django 4.1 on 2022-10-02 19:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("likes", "0002_alter_likeditem_object_id"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="LikedItem",
            new_name="Like",
        ),
    ]