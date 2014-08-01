from django.shortcuts import render
from django.http import *
import numpy as np
from graph import *

# Create your views here.

def home(request):
    districts = np.loadtxt( 'data.csv',
                        delimiter=',',
                        unpack=True,
                        dtype='str')

    #population = [float(((i+j)[1:-1].strip())) for i,j in zip(districts[2][1:],districts[3][1:])]
    vaccinated = '0'
    infected = 0
    epidemic_name = ''
    if request.method == 'POST':
        district = request.POST.get('district')
        infected = int(request.POST.get('infected'))
        _ = request.POST.get('vaccinated','0')
        if _=='': _ = '0'
        vaccinated = int(_)
        epidemic_name = request.POST.get('epidemic')
        gen_graph(district, infected, vaccinated, epidemic_name, districts[0][1:],districts[2][1:])
    return render(request, "index.html",{'districts':districts[0][1:],'infected':infected,'vaccinated':vaccinated,'epidemic_name':epidemic_name})

def image(request):
    a = HttpResponse(open('Nepal_Zones.svg','r').read(),mimetype="image/svg+xml")
    return a

def genmap(request):
    # print "GenMap"
    a = HttpResponse(open('NepalMap.svg','r').read(),mimetype="image/svg+xml")
    return a

# home()