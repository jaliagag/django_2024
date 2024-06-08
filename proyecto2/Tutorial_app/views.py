from django.shortcuts import render
from django.http import HttpResponse
from tabulate import tabulate


def inicio(request):
    table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]

    print(tabulate(table, tablefmt='html'))
    nombre = {"nombre": "jose"}
    return render(request, "Tutorial_app/index.html", nombre)
    #return HttpResponse('vista inicio')

def dashboards(request):
    return render(request, "Tutorial_app/dashboard.html")
    #return HttpResponse('vista dashboards')

def login(request):
    return render(request, "Tutorial_app/login.html")
    #return HttpResponse('vista login')
