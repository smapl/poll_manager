from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Poll, UserAnswer, Questions
from .utils import poll_questions

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

        return JsonResponse({"result": poll_list})

    else:
        return JsonResponse({"result": "bad request"})


@csrf_exempt
def get_poll(request):
    if request.method == "GET" and len(request.body) != 0:
        body_request = json.loads(request.body.decode("utf-8"))
        search_filter = body_request["filter"]
        poll_id = search_filter["id"]

        poll_by_id = Poll.objects.filter(id=poll_id)
        poll_by_id = poll_by_id.values()[0]

        questions_ids = poll_by_id["questions_ids"]
        question_dict = poll_questions(Questions, questions_ids)

        poll_by_id["quiestions"] = question_dict
        poll_by_id["poll_id"] = poll_by_id["id"]

        poll_by_id.pop("questions_ids", None)
        poll_by_id.pop("id", None)

        return JsonResponse(poll_by_id)

    else:
        return JsonResponse({"result": "bad request"})


@csrf_exempt
def send_poll_answer(request):
    if request.method == "POST":
        data = dict()
        try:
            data["poll_id"] = int(request.POST.get("poll_id"))
            data["user_id"] = int(request.POST.get("user_id"))
            data["answers"] = request.POST.get("answers")

        except Exception as ex:
            logger.error(ex)
            return JsonResponse({"response": "error"})

        try:
            request_to_db = UserAnswer(
                poll_id=data["poll_id"],
                user_id=data["user_id"],
                answers=data["answers"],
            )
            request_to_db.save()
        except Exception as ex:
            logger.error(ex)
            return JsonResponse(
                {"result": "server error. cannot save data to database"}
            )
    else:
        return JsonResponse({"result": "bad request"})


@csrf_exempt
def get_passed_polls(request):
    if request.method == "GET" and len(request.body) != 0:
        body_request = json.loads(request.body.decode("utf-8"))
        search_filter = body_request["filter"]
        user_id = search_filter["user_id"]

        passed_polls = UserAnswer.objects.filter(user_id=user_id)
        passed_poll_list = [poll for poll in passed_polls.values()]

        for passed in passed_poll_list:
            poll_id = passed["poll_id"]
            poll_by_id = Poll.objects.filter(id=poll_id)
            poll_by_id = poll_by_id.values()[0]
            poll_by_id.pop("quiestions_ids", None)

            questions_ids = poll_by_id["questions_ids"]
            questions = poll_questions(Questions, questions_ids)

            passed["poll"] = poll_by_id
            passed["questions"] = questions

        return JsonResponse({"result": passed_poll_list})
    else:
        return JsonResponse({"result": "bad request"})
