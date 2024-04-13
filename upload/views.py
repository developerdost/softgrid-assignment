import os
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.db import transaction
from django.core.files import File
from django.http import FileResponse
from django.core.exceptions import PermissionDenied
# ....
from .models import UploadedFile, app_name
from .forms import UploadFileForm
from . import crypto


class ListView(LoginRequiredMixin, generic.ListView):
    template_name = 'upload/list.html'
    model = UploadedFile
    context_object_name = 'objects'
    extra_context = {
        'add_url': reverse_lazy(f'{app_name}:create')
    }

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(ref_user=self.request.user)



class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'upload/create.html'
    model = UploadedFile
    form_class = UploadFileForm
    success_url = reverse_lazy(f'{app_name}:list')
    extra_context = {
        'cancel_url': reverse_lazy(f'{app_name}:list')
    }

    @transaction.atomic()
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        object = form.save(commit=False)
        file_name = object.file.name
        file_path = object.file.path
        
        with open(file_path, 'wb') as file:
            content = b''
            for chunk in object.file.chunks():
                content += chunk

            file.write(crypto.encrypt_data(settings.ENCRYP_KEY, settings.ENCRYP_IV, content))
        
        object.file = File(name=file_name, file=open(file_path, 'rb'))        
        object.ref_user = self.request.user
        
        os.remove(file_path)
        
        object.save()

        return super().form_valid(form)



class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'upload/delete.html'
    model = UploadedFile
    success_url = reverse_lazy(f'{app_name}:list')
    extra_context = {
        'cancel_url': success_url
    }


class DownloadFileView(generic.View):

    def get(self, request, *args, **kwargs):
        file_id = self.kwargs.get('pk')
        # get file object
        file_obj = get_object_or_404(UploadedFile, pk=file_id)
        # decrypt that file 
        with open(file_obj.file.path, 'rb') as file:
            content = file.read()

        original_content = crypto.decrypt_data(settings.ENCRYP_KEY, settings.ENCRYP_IV, content)

        with open(f'/tmp/{file_obj.file.name.split("/")[-1]}', 'wb') as file:
            file.write(original_content)

        response = FileResponse(
            File(name=file_obj.file.name, file=open(f'/tmp/{file_obj.file.name.split("/")[-1]}', 'rb')) , 
            as_attachment=True, 
            filename=file_obj.file.name)

        file_obj.increment_downloads
        
        return response
    




class ToggleStatusView(LoginRequiredMixin, generic.View):
    model = UploadedFile
    http_method_names = ['get']
    success_url = reverse_lazy(f'{app_name}:list')

    
    def get(self, request, *args, **kwargs):
        object_id = self.kwargs.get('pk')


        if self.model:
            object = get_object_or_404(self.model, pk=object_id)
            # Check the current user with object user
            if (not request.user == object.ref_user):
                raise PermissionDenied()


            object.toggle_object_status

            return redirect(self.success_url)
        
        return HttpResponse('something went wrong')