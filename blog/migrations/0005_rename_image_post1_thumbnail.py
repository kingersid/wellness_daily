# Generated by Django 4.2.1 on 2023-06-02 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post1_tags_delete_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post1',
            old_name='image',
            new_name='thumbnail',
        ),
    ]