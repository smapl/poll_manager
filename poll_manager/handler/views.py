from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Poll, UserAnswer, Questions
from .utils import dict_generate

from loguru import logger

import json


@csrf_exempt
def active_polls(request):
    if request.method == "GET" and len(request.body) != 0:
        body_request = json.loads(request.body.decode("utf-8"))
        search_filter = body_request["filter"]
        status = search_filter["status"]

        access_polls = Poll.objects.filter(poll_status=status)
        poll_list = [poll for poll in access_polls.values()]
        logger.info(poll_list)
        return JsonResponse({"result": poll_list})

    else:
        return JsonResponse({"result": "bad request"})


@csrf_exempt
def get_poll(request):
    if request.method == "GET" and len(request.body) != 0:
        pass

    else:
        return JsonResponse({"result": "bad request"})


@csrf_exempt
def send_poll_answer(request):
    if request.method == "POST":
        pass
    else:
        return JsonResponse({"result": "bad request"})
