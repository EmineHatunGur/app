# Generated by Django 4.0.4 on 2022-05-10 14:48

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='article_images')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='category_name', unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name_surname', models.CharField(max_length=150)),
                ('mesaj', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'iletisim',
                'verbose_name_plural': 'iletisims',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
                ('contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(max_length=100, related_name='article', to='app.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
