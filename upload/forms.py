from django import forms
# ....
from .models import UploadedFile



class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadedFile
        fields = ('file', )

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['file'].widget.attrs.update({'class': 'form-control'})