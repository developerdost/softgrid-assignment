from django.contrib import admin
from django.urls import path, include
# ....
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DashboardView.as_view(), name='dashboard'),

    path('accounts/', include('account.urls')),
    path('files/', include('upload.urls')),
]
