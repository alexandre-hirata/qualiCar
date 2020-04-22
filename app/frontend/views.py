from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from qualiCar_API.models import UserProfile



# class Index (APIView):
#     template = 'index.html'

class Index(View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        return render(request, self.template)


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
