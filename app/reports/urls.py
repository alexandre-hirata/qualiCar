from django.contrib import admin
from django.urls import path, include

from reports import views

urlpatterns = [
    path ('parts/import', views.import_data, name = 'import-parts'),
    path ('parts/export', views.export_data, name = 'export-parts'),
]
