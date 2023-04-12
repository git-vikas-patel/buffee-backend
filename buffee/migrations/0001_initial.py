# Generated by Django 4.1.8 on 2023-04-12 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField()),
                ('synopsis', models.TextField()),
                ('genre', models.CharField(max_length=200)),
                ('cast_and_crew', models.TextField()),
                ('production_companies', models.CharField(max_length=200)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('runtime', models.PositiveIntegerField()),
                ('cover_art_url', models.URLField()),
                ('trailer_and_video', models.TextField()),
                ('reviews_and_ratings', models.TextField()),
                ('download_links_480p', models.URLField()),
                ('download_links_720p', models.URLField()),
                ('download_links_1080p', models.URLField()),
                ('download_links_4k', models.URLField()),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='buffee.movie')),
            ],
        ),
    ]
