from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, Mundo. You're at the polls index.")

