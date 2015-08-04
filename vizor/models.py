# -*- coding:utf-8 -*-

import os
import unicodedata
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from model_utils.fields import StatusField
from model_utils import Choices


fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class FileUpload(models.Model):
    
    filename = models.FileField(default=None,storage=fs)
    def __unicode__(self):
        return self.name

    def name(self):
        return self.name

    def url(self):
        return settings.BASE_DIR + self.filename.url


class Encode(models.Model):
    frmt = models.CharField(null=True, blank=True, max_length=10)

    def __unicode__(self):
        return self.frmt 


class VideoBitrate(models.Model):
    vbitrate = models.CharField(null=True, blank=True, max_length=10)
    def __unicode__(self):
        return self.vbitrate


class AudioBitrate(models.Model):
    abitrate = models.CharField(null=True, blank=True, max_length=10)
    def __unicode__(self):
        return self.abitrate


class FrameSize(models.Model):
    size = models.CharField(null=True, blank=True, max_length=16)
    def __unicode__(self):
        return self.size


class AspectRatio(models.Model):
    ratio = models.CharField(null=True, blank=True, max_length=16)
    def __unicode__(self):
        return self.ratio


class AudioCodec(models.Model):
    acodec = models.CharField(null=True, blank=True, max_length=16)
    def __unicode__(self):
        return self.acodec


class VideoCodec(models.Model):
    vcodec = models.CharField(null=True, blank=True, max_length=16)
    def __unicode__(self):
        return self.vcodec


class Uploaded(models.Model):
    name = models.CharField(max_length=124)
    url = models.CharField(max_length=124)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Uploaded"

    def __unicode__(self):
        return self.name


class Files(models.Model):

    STATUS = Choices('unconverted', 'converted')

    status = StatusField() 
    name = models.ForeignKey(Uploaded, related_name="filename")
    format = models.ForeignKey(Encode)
    audiocodec = models.ForeignKey(AudioCodec)
    audiobitrate = models.ForeignKey(AudioBitrate)
    videocodec = models.ForeignKey(VideoCodec)
    videobitrate = models.ForeignKey(VideoBitrate)
    aspectratio = models.ForeignKey(AspectRatio)
    framesize = models.ForeignKey(FrameSize)

    class Meta:
        verbose_name_plural = "Files"


class Exposed(models.Model):
    name = models.CharField(max_length=256, null=True)
    link = models.CharField(max_length=256, null=True)

    class Meta:
        verbose_name_plural = "Exposed"
