from django.shortcuts import render
import json
from django.http import HttpResponse
from tabulate import tabulate

# https://wpdatatables.com/table-with-collapsible-rows/
def inicio(request):
    table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]

    # make = tabulate(table, tablefmt='html')
    with open(file='Tutorial_app/response_ocp.json') as f:
        myj = json.loads(f.read())
        nombre = {"data": table, "json": myj}
        return render(request, "Tutorial_app/index.html", nombre )
    #return HttpResponse('vista inicio')

def dashboards(request):
    return render(request, "Tutorial_app/dashboard.html")
    #return HttpResponse('vista dashboards')

def login(request):
    return render(request, "Tutorial_app/login.html")
    #return HttpResponse('vista login')
