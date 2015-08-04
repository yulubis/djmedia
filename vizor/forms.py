# -*- coding:utf-8 -*-

from django import forms
from models import FileUpload 


class FileUploadForm(forms.ModelForm):

    class Meta:

        model = FileUpload 
        fields = ('filename',)
