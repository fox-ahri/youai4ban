from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view()),
    path('index/<id>/', views.IndexView.as_view()),
]
