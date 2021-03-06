from django.urls import path, include

from rest_framework.routers import DefaultRouter

# This import is from qualiCar
from qualiCar_API import views


app_name = 'qualiCar_API'

router = DefaultRouter ()
# Does not require base-name because there is queryset in Viewset
# Base-name is required if there is no queryset or overwriting the name of the queryset
router.register ('profile', views.UserProfileViewSet)
router.register ('date', views.DateViewSet)
router.register ('part', views.PartViewSet)
router.register ('vehicle', views.VehicleViewSet)
router.register ('incident', views.IncidentViewSet)

urlpatterns = [
    path ('hello-view/', views.qualiCarApiView.as_view()),
    path ('login/', views.UserLoginApiView.as_view ()),
    path ('', include (router.urls))
]
