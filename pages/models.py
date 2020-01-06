from django.db import models
from django.dispatch import receiver

class SocialInfo(models.Model):
    twitchchannel = models.URLField(verbose_name='twitch_channel', null=True, blank=True,
                                    default='https://www.twitch.tv')
    youtubechannel = models.URLField(verbose_name='youtube_channel', null=True, blank=True,
                                     default='https://www.youtube.com')
    twitterprofile = models.URLField(verbose_name='twitter_profile', null=True, blank=True,
                                     default='https://www.twitter.com')
    facebookpage = models.URLField(verbose_name='facebook_page', null=True, blank=True,
                                   default='https://www.facebook.com')
    instagrampage = models.URLField(verbose_name='instagram_page', null=True, blank=True,
                                    default='https://www.instagram.com')

    stream = models.CharField(default='twitch', max_length=25)


class StaticInfo(models.Model):
    about_us = models.TextField(default='about us')
    terms = models.TextField(default='terms of service')
