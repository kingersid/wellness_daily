# Generated by Django 4.2.1 on 2023-06-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='post1',
            name='tags',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]
