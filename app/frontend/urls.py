from django.urls import path, include
from frontend import views
from django.contrib import admin


urlpatterns = [
    path('', views.Index.as_view (), name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('admin', admin.site.urls, name='admin'),
    path('incident', views.Incident.as_view (), name='incident'),
]
