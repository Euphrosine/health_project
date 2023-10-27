from django.shortcuts import render
from django.http import JsonResponse
from .models import HealthData
from django.utils import timezone


# Create your views here.
# http://127.0.0.1:8000/chart_data/?bim=15&temperature=16&spo2=18&strick=20&bp=16
def chart_data_view(request):
    bim = request.GET.get('bim', None)
    temperature = request.GET.get('temperature', None)
    spo2 = request.GET.get('spo2', None)
    strick = request.GET.get('strick', None)
    bp = request.GET.get('bp', None)

    # Create a dictionary to store the data you want to save
    data_to_save = {
        'timestamp': timezone.now(),
        'bim': bim,
        'temperature': temperature,
        'strick': strick,
        'bp': bp,
    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    HealthData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})

def display_chart_data(request):
    health_data = HealthData.objects.all()
    return render(request, 'health_app/chart_data_view.html', {'health_data': health_data})


def index(request):
    return render(request,'health_app/index.html')

def add_temp(request):
    return render(request,'health_app/add_temperature.html')


