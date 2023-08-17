from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from consumer.models import Customer, Orders
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from dealership.models import CarDealer, Area, Vehicles
from django.http import HttpResponseRedirect

# Create your views here.

def index_page(request):
    context = {}
    if not request.user.is_authenticated:
        return render(request, 'consumertemp/login.html', context)
    else:
        return render(request, 'consumertemp/home.html', context)
    
def login_page(request):
    context = {}
    return render(request, 'customertemp/login.html', context)

def auth_view(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'customertemp/home.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            customer = Customer.objects.get(user=user)
        except:
            customer = None
        if customer is not None and customer.is_active == True:
            auth.login(request, user)
            return render(request, 'customertemp/home.html', context)
        else:
            return render(request, 'customertemp/index.html', context)

def logout_page(request):
    context = {}
    auth.logout(request)
    return render(request, 'customertemp/register.html', context)

def register(request):
    context = {}
    return render(request, 'customertemp/register.html', context)

def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    city = request.POST['city']
    city = city.lower()
    pincode = request.POST['pincode']
    
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'customertemp/home.html')
    try:
        area = Area.objects.get(city=city, pincode=pincode)
    except:
        area = None
    if area is not None:
        customer = Customer(user=user, mobile=mobile, area=area)
    else:
        area = Area(city=city, pincode=pincode)
        area.save()
        customer = Customer(user=user, mobile=mobile, area=area)
    
    context = {}
    customer.save()
    return render(request, 'customertemp/register.html', context)

@login_required
def search(request):
    context = {}
    return render(request, 'customertemp/search.html', context)

@login_required
def searchResult(request):
    city = request.POST['city']
    city = city.lower()
    vehiclesList = []
    area = Area.objects.filter(city=city)
    for a in area:
        vehicles = Vehicles.objects.filter(area=a)
        for v in vehicles:
            if v.is_available == True:
                vehicleDict = {'name': v.car_name, 'color': v.color, 'pincode': v.area.pincode, 'capacity': v.capacity, 'description': v.description}
                vehiclesList.append(vehicleDict)
    request.session['vehicles_list'] = vehiclesList
    context = {}
    return render(request, 'customertemp/searchresult.html', context)

@login_required
def bookVehicle(request):
    id = request.POST['id']
    vehicle = Vehicles.objects.get(id=id)
    costPerDay = int(vehicle.capacity)*3000
    context = {'vehicle': vehicle, 'cost_per_day': costPerDay}
    return render(request, 'customertemp/confirmation.html', context)

@login_required
def confirmBooking(request):
    vehicleId = request.POST['id']
    username = request.user
    user = User.objects.get(username=username)
    days = request.POST['days']
    vehicle = Vehicles.objects.get(id=vehicleId)
    
    if vehicle.is_available:
        carDealer = vehicle.dealer
        rent = (int(vehicle.capacity))*(int(days))*3000
        carDealer.wallet += rent
        carDealer.save()
        
        try:
            order = Orders(vehicle=vehicle, car_dealer=carDealer, user=user, rent=rent, days=days)
            order.save()
        except:
            order = Orders(vehicle=vehicle, car_dealer=carDealer, user=user, rent=rent, days=days)
        vehicle.is_available = False
        vehicle.save()
        context = {'order': order}
        return render(request, 'customertemp/confirmed.html', context)
    
    else:
        return render(request, 'customertemp/orderfail.html')
    
@login_required
def manage(request):
    order_list = []
    user = User.objects.get(username = request.user)
    try:
        orders = Orders.objects.filter(user=user)
    except:
        orders = None
    if orders is not None:
        for order in orders:
            if order.is_complete == False:
                orderDict = {'id': order.id, 'rent': order.rent, 'vehicle': order.vehicle, 'days': order.days, 'car_dealer': order.car_dealer}
                order_list.append(orderDict)
    context = {'od': order_list}
    return render(request, 'customertemp/manage.html', context)

@login_required
def update_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id=order_id)
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    carDealer = order.car_dealer
    carDealer.wallet -= int(order.rent)
    carDealer.save()
    order.delete()
    costPerDay = int(vehicle.capacity)*3000
    context = {'vehicle': vehicle, 'cost_per_day': costPerDay}
    return render(request, 'customertemp/confirmation.html', context)

@login_required
def delete_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id=order_id)
    carDealer = order.car_dealer
    carDealer.wallet -= int(order.rent)
    carDealer.save()
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    order.delete()
    context = {}
    return render(request, 'customertemp/manage.html', context)
    
    