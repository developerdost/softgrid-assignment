from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
# ....
from upload.models import UploadedFile


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'


    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        user_files = UploadedFile.objects.filter(ref_user=self.request.user)

        context['total_uploads'] = user_files.count()
        context['total_downloads'] = user_files.aggregate(total_downloads=Sum('download', default=0))['total_downloads']

        return context