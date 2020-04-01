from django.shortcuts import render
from rest_framework.views import APIView

from django.http import HttpResponse
from django.template import loader


# class Index (APIView):
#     template = 'index.html'

def Index (request):
    return render(request, 'index.html')
