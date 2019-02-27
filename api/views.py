from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import uuid


from .models import Graph

def home(request):
    return render(request,'api/home.html')


def get_mq(request):
    try:
        data=json.loads(request.body.decode())
        obj = Graph()
        id=uuid.uuid4()
        obj.sender = data['sender']
        obj.msg_type= data['msg_type']
        obj.receiver=data['receiver']
        obj.frequency=data['freq']
        obj.save()
        return JsonResponse({'success': 1})
    except:
        return JsonResponse({'success': 0})

def get_data(request):
    lst=list(Graph.objects.all())
    return JsonResponse({'items':lst})
