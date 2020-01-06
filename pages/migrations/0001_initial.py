# Generated by Django 2.2.2 on 2020-01-06 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitchchannel', models.URLField(blank=True, default='https://www.twitch.tv', null=True, verbose_name='twitch_channel')),
                ('youtubechannel', models.URLField(blank=True, default='https://www.youtube.com', null=True, verbose_name='youtube_channel')),
                ('twitterprofile', models.URLField(blank=True, default='https://www.twitter.com', null=True, verbose_name='twitter_profile')),
                ('facebookpage', models.URLField(blank=True, default='https://www.facebook.com', null=True, verbose_name='facebook_page')),
                ('instagrampage', models.URLField(blank=True, default='https://www.instagram.com', null=True, verbose_name='instagram_page')),
                ('stream', models.CharField(default='twitch', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StaticInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(default='about us')),
                ('terms', models.TextField(default='terms of service')),
            ],
        ),
    ]
