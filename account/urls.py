from django.urls import path
from pathlib import Path
# ....
from . import views


app_name = Path(__file__).resolve().parent.name



urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]