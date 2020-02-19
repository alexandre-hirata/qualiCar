from django.urls import path

# This import is from qualiCar
from qualiCar_API import views

urlpatterns = [
    path ('hello-view/', views.qualiCarApiView.as_view()),
]
