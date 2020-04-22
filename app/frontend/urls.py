from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.Index.as_view (), name='index'),
    path('login', views.Login.as_view(), name='login'),
]
