# -*- coding:utf-8 -*-

import os
import shutil
import subprocess
from django.conf import settings


def convertor(filename, frmt, vbitrate, abitrate, size, ratio, acodec, vcodec):
    location = settings.MEDIA_ROOT+'/'
    filename = filename.replace(' ', '_').translate(None, ",()")
    path = location + filename
    os.chdir(location)
    if os.path.isfile(path):
        name, ext = os.path.splitext(filename)
        newname = name+'.'+frmt 
        subprocess.call(['ffmpeg',
            '-i', filename,
            '-acodec', acodec,
            '-b:a', abitrate,
            '-vcodec', vcodec,
            '-b:v', vbitrate,
            '-aspect', ratio,
            '-s', size,
            newname
            ], 
        )
        return newname, path
    else:
        return 'File does not exist'
