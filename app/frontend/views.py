from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from qualiCar_API.models import UserProfile, Incident, Vehicle, Part
from qualiCar_API.serializers import incidentSerializer
from frontend.forms import IncidentForm

import logging


logger = logging.getLogger (__name__)

def preprocess_request(request):
    if isinstance(request, HttpRequest):
        return Request(request, parsers=[FormParser])
    return request

# class Index (APIView):
#     template = 'index.html'

class Index(View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)


class Incident (APIView):
    logger.info ("Incident view")
    template = 'forms/incident.html'
    context = {}
    context['form'] = IncidentForm

    # incident_part = Incident.objects.get (request.)
    # array2=[]
    # for single_vehicle in Vehicle.objects.all():
    #     flag = False
    #     for vehicle_part in single_vehicle.parts.all():
    #         if (vehicle_part == incident_part):
    #             flag = True
    #     if flag:
    #         array2.append (vehicle)


    model = Incident
    #form_class = IncidentForm


    def get(self, request):
        logger.info ("Incident view get method")
        context = {}
        context ['form'] = IncidentForm
        return render(request, self.template, context)

    def post (self, request):
        logger.info ("Incident view post method")

        form = AuthenticationForm (request.POST)

        serializer = incidentSerializer (
        # Pass the context resolves the KeyError request
            context = {'request': request},
            data = request.data,
        )

        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login (View):
    template = 'login.html'

    def get (self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post (self, request):
        form = AuthenticationForm (request.POST)
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login (request, user)
            return HttpResponseRedirect ('/')
        else:
            return render (request, self.template, {'form': form})


def load_vehicles (request):
    part_id = request.GET.get ('parts')
    vehicles = Vehicle.objects.filter (part_id = part_id).order_by ('brand')

    # I do not know if it is vehicles:vehicles, actually... Maybe all fields???
    return render
    (
        request,
        'forms/dyn/impacted_vehicles_table.html',
        {'vehicles': vehicles}
    )
