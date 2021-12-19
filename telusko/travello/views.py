from django.shortcuts import render
from .models import Destination
# Create your views here.
 
def index(request):
    dest1 = Destination()
    dest1.name = "MUMBAI"
    dest1.id =1
    dest1.price = 400
    dest1.img = 'destination_1.jpg'
    dest1.desc = "The city of dreams"
    dest1.offer = True

    dest2 = Destination()
    dest2.name = "BANGALORE"
    dest2.id =1
    dest2.price = 599
    dest2.img = 'destination_2.jpg'
    dest2.desc = "The city of IT hub"
    dest2.offer = False

    dest3 = Destination()
    dest3.name = "KOLKATA"
    dest3.id =1
    dest3.price = 388
    dest3.img = 'destination_3.jpg'
    dest3.desc = "The city of dreams"
    dest3.offer = True

    dest4 = Destination()
    dest4.name = "NEW DELHI"
    dest4.id =1
    dest4.price = 500
    dest4.img = 'destination_4.jpg'
    dest4.desc = "The city of dreams"
    dest4.offer = True
    
    dests = [dest1,dest2,dest3,dest4]
    return render(request,"index.html", {'dests' : dests})





