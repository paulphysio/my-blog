# Generated by Django 4.0.4 on 2022-06-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_profile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]