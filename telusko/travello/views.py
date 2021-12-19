from django.shortcuts import render
from .models import Destination
# Create your views here.
 
def index(request):
    dests = Destination.objects.all()  #it will fetch all the datas from the database
    return render(request,"index.html", {'dests' : dests})





