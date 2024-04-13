import os
from uuid import uuid4
from pathlib import Path
from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
# ....


app_name = Path(__file__).resolve().parent.name



def get_file_path(instance, filename):
    return os.path.join(str(instance.ref_user.username), filename)



class UploadedFile(models.Model):

    id = models.UUIDField(
        verbose_name=_('Id'),
        primary_key=True,
        default=uuid4,
        editable=False
    )

    file = models.FileField(
        verbose_name=_('File'),
        upload_to=get_file_path
    )

    ref_user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        verbose_name=_('Select User'),
    )

    download = models.PositiveIntegerField(
        verbose_name=_('Downloads'),
        editable=False,
        default=0,
    )

    # can_share = models.BooleanField(
    #     verbose_name=_('Can Share'),
    #     editable=False,
    #     default=False,
    # )

    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        default=True
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created At'),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name=_('Updated At'),
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Uploaded File')
        verbose_name_plural = _('Uploaded Files')
        ordering = ('-created_at',)


    def __str__(self) -> str:
        return self.file.name.split('/')[-1]
    
    
    @property
    def increment_downloads(self):
        self.download += 1
        self.save()

    @property
    def toggle_object_status(self):
        self.is_active = not self.is_active
        self.save()
    

    @transaction.atomic()
    def delete(self, *args, **kwargs):
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)

        super().delete(*args, **kwargs)



    @property
    def download_url(self):
        return reverse_lazy(f'{app_name}:download', kwargs={'pk': self.pk})

    @property
    def status_url(self):
        return reverse_lazy(f'{app_name}:status', kwargs={'pk': self.pk})

    @property
    def delete_url(self):
        return reverse_lazy(f'{app_name}:delete', kwargs={'pk': self.pk})

    @property
    def share_url(self):
        return reverse_lazy(f'{app_name}:share', kwargs={'pk': self.pk})