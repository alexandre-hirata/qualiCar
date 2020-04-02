from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('login', views.Login.as_view(), name='login'),
]
