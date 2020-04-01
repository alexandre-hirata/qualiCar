from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.Index, name='index'),
]
