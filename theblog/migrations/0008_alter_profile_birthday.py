# Generated by Django 4.0.4 on 2022-05-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_remove_profile_email_remove_profile_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default='2000-12-31', max_length=200, null=True),
        ),
    ]
