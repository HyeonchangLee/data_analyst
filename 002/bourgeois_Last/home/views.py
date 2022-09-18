from django.shortcuts import render
import cx_Oracle as ora
import json
from django.http import JsonResponse


def web(request):
    return render(request, 'web.html')


def web_admin(request):
    return render(request, 'web_admin.html')