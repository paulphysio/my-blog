# Generated by Django 4.0.4 on 2022-06-19 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0023_alter_friend_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friend',
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='friend', to='theblog.friend'),
        ),
    ]
