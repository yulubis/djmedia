# -*- coding:utf-8 -*-

import os
from os import listdir
from os.path import isfile, join
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.conf import settings
from vizor.convertor import convertor
from vizor.models import Uploaded, Encode, VideoBitrate, Files, AudioBitrate, AspectRatio, AudioCodec, VideoCodec, FrameSize, Exposed


class VideoAdminSite(AdminSite):
    site_title = ugettext_lazy('Video admin')
    site_header = ugettext_lazy('Video administration')
    index_title = ugettext_lazy('Video administration')

admin_site = VideoAdminSite()


class EncodeAdmin(admin.ModelAdmin):
    list_display = ('frmt',)
    fieldsets = (
            (None, {
        'fields': ('frmt',),
        'description': "Convert to (e.g. 'mp4', 'flv')"
        }),
    )
   
class VideoBitrateAdmin(admin.ModelAdmin):
    list_display = ('vbitrate',)
    fieldsets = (
            (None, {
        'fields': ('vbitrate',),
        'description': "Append 'k' to value or kilobits (e.g. '1200k)"
        }),
    )
    class Meta:
        verbose_name = "Video Bitrate"
    
class UploadedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url') 

class AudioBitrateAdmin(admin.ModelAdmin):
    list_display = ('abitrate',)

class AspectRatioAdmin(admin.ModelAdmin):
    list_display = ('ratio',)

class FrameSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

class AudioCodecAdmin(admin.ModelAdmin):
    list_display = ('acodec',)

class VideoCodecAdmin(admin.ModelAdmin):
    list_display = ('vcodec',)

class ExposedAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'format', 'audiocodec', 'audiobitrate', 'videocodec', 'videobitrate', 'aspectratio', 'framesize', 'status')
    exclude = ('status', 'path')
    actions = ['convert'] 

    def convert(FilesAdmin, request, queryset):
        for i in range(len(queryset)):
            filename = str(queryset[i].name)
            frmt = str(queryset[i].format)
            vbitrate = str(queryset[i].videobitrate)
            abitrate = str(queryset[i].audiobitrate)
            size = str(queryset[i].framesize)
            ratio = str(queryset[i].aspectratio)
            acodec = str(queryset[i].audiocodec)
            vcodec = str(queryset[i].videocodec)
            info = convertor(filename, frmt, vbitrate, abitrate,
                            size, ratio, acodec, vcodec)
            if info:
                queryset.update(status='converted')
            name = info[0]
            link = os.path.join(settings.MEDIA_URL, name)
            exposed = Exposed(name=name, link=link)
            exposed.save()
    convert.short_description = "Convert Selected"


admin_site.register(Uploaded, UploadedAdmin)
admin_site.register(Encode, EncodeAdmin)
admin_site.register(VideoBitrate, VideoBitrateAdmin)
admin_site.register(Files, FilesAdmin)
admin_site.register(AspectRatio, AspectRatioAdmin)
admin_site.register(AudioBitrate, AudioBitrateAdmin)
admin_site.register(FrameSize, FrameSizeAdmin)
admin_site.register(AudioCodec, AudioCodecAdmin)
admin_site.register(VideoCodec, VideoCodecAdmin)
admin_site.register(Exposed, ExposedAdmin)
