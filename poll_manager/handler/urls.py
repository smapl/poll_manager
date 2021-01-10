from django.urls import path, include
from .views import active_polls, get_poll, send_poll_answer, get_passed_polls

urlpatterns = [
    path("api/active_polls", active_polls, name="active_polls"),
    path("api/get_poll", get_poll, name="get_poll"),
    path("api/send_poll_answer", send_poll_answer, name="send_poll_answer"),
    path("api/get_passed_polls", get_passed_polls, name="get_passed_polls"),
]
