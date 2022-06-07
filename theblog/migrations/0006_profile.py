# Generated by Django 4.0.4 on 2022-05-25 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0005_blogpost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=200, null=True)),
                ('linkedIn_url', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('twitter_url', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('instagram_url', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('facebook_url', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/images')),
                ('birthday', models.DateField(blank=True, default='', max_length=200, null=True)),
                ('age', models.PositiveIntegerField(blank=True, default='', null=True)),
                ('skill_1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('skill_2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bio', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('website', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('degree', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('freelance', models.CharField(default='Unavailable', max_length=20)),
                ('about_image', models.ImageField(blank=True, null=True, upload_to='about_images')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]