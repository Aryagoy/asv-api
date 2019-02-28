from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import uuid
import datetime
import math
from django.views.decorators.csrf import csrf_exempt

from .models import Graph, Log
from dashboard.models import Horizon, Scan

@csrf_exempt
@require_POST
def set_mq(request):
    try:
        data=json.loads(request.body.decode())
        obj = Graph()
        id=uuid.uuid4()
        obj.sender = data['sender']
        obj.msg_type= data['msgType']
        obj.receiver=data['receiver']
        obj.frequency=data['freq']
        obj.save()
        return JsonResponse({'success': True})
    except:
        return JsonResponse({'success': False})

@csrf_exempt
@require_POST
def set_logs(request):
    try:
        data=json.loads(request.body.decode())
        obj = Log()
        id = uuid.uuid4()
        obj.name = data["name"]
        obj.level = int(data.get("level", 0))
        obj.message = data["message"]
        obj.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})

@csrf_exempt
@require_POST
def set_horizon(request):
    try:
        data=json.loads(request.body.decode())
        obj = Horizon.objects.all()
        if(len(obj)==0):
            obj = Horizon()
        else:
            obj = obj[0]
        obj.roll = data.get("roll")
        obj.pitch = data.get("pitch")
        obj.accel = data.get("accel")
        obj.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})

@csrf_exempt
@require_POST
def set_scan(request):
    try:
        data=json.loads(request.body.decode())
        obj = Scan.objects.all()
        if(len(obj)==0):
            obj = Scan()
        else:
            obj = obj[0]
        obj.start_angle = data["angleMin"]
        obj.stop_angle = data["angleMax"]
        obj.angle_increment = data["angleIncrement"]
        obj.range_min = data["rangeMin"]
        obj.range_max = data["rangeMax"]
        obj.ranges = data["ranges"]
        obj.intensities = data["intensities"]
        obj.save()
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})

@csrf_exempt
def get_scan(request):
    latest = Scan.objects.latest("id")
    return JsonResponse({ "start_angle": math.degrees(latest.start_angle)%360, "stop_angle": math.degrees(latest.stop_angle), "angle_increment": math.degrees(latest.angle_increment), \
    "range_min": latest.range_min, "range_max": latest.range_max, "ranges": latest.ranges, "intensities": latest.intensities})

@csrf_exempt
def get_horizon(request):
    latest = Horizon.objects.latest("time_received")
    return JsonResponse({"pitch": latest.pitch, "roll": latest.roll, "accel": latest.accel})
