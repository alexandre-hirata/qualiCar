from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
from django.template import loader


# class Index (APIView):
#     template = 'index.html'

def Index (request):
    return render(request, 'index.html')


class Login (View):
    template = 'login.html'

    def get (self, request):
        return render(request, self.template)
