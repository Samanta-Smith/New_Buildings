from django.shortcuts import render
from .models import House,Brick
from .forms import HouseForm
from django.http import HttpResponseRedirect




def new(request):
    if request.method == "POST":
        house = House()
        house.address = request.POST.get("address")
        house.year = request.POST.get("year")
        house.save()
        bricks = Brick()
        bricks.house = house
        bricks.save()
    return HttpResponseRedirect("/")
def add(request,id):
    house = House.objects.get(pk=id)
    bri = Brick.objects.get(house=house)
    bri.num +=10
    bri.save()
    return HttpResponseRedirect("/")
def stats(request):
    data = {
    'houses': House.objects.all().order_by('year'),
    'HouseForm' : HouseForm(),
    }
    return render(request,'index.html',data)


# Create your views here.
