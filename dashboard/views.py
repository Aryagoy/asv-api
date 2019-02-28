from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.

def get_dashboard(request):
    return render(request, "dashboard/horizon.html")
