from django.urls import path
from . import views_login, views_admin, views_upload

urlpatterns = [
    path('login/', views_login.LoginView.as_view()),
    path('admin/', views_admin.AdminView.as_view()),
    path('upload/', views_upload.UploadView.as_view()),
]
