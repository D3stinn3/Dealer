from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'hometemp/home.html', context)