# -*- coding:utf-8 -*-

import os
import mimetypes
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import StreamingHttpResponse
from django.conf import settings
from django.utils.encoding import smart_str
from vizor.forms import FileUploadForm 
from vizor.models import FileUpload, Uploaded, Files, Exposed


def index(request):
    input_list = Uploaded.objects.all()
    output_list = Exposed.objects.all()
    context_dict = {'upload': input_list, 
                    'download': output_list}
    return render(request, 'index.html', context_dict)
    


def upload_handler(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST or None, 
                              request.FILES or None)
        if form.is_valid():
            form.save(commit=True)
            uploaded_file_info(request.FILES['filename'])
            return HttpResponseRedirect('/')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})


def uploaded_file_info(filename):
    name = filename.name
    url = os.path.join(settings.MEDIA_ROOT, name)
    uploaded = Uploaded(name=name, url=url)
    uploaded.save()


def download(request, filename):
    file_path = settings.MEDIA_ROOT +'/'+ filename

    # Streaming file in chunks without loading it in memory
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(file_path), chunk_size), content_type=mimetypes.guess_type(file_path)[0])
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename) 
    return response
