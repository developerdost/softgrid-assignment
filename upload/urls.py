from django.urls import path
# ....
from . import views


app_name = views.app_name


urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('upload/', views.CreateView.as_view(), name='create'),
    path('<uuid:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<uuid:pk>/download/', views.DownloadFileView.as_view(), name='download'),
    path('<uuid:pk>/status/', views.ToggleStatusView.as_view(), name='status'),
    path('<uuid:pk>/share/', views.DownloadFileView.as_view(), name='share'),
]