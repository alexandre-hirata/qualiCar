from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
from django.template import loader


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
        return render(request, self.template)
