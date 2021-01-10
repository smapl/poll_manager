from django.db import models


class Poll(models.Model):
    ACTIVE = "active"
    DEACTIVED = "deactived"
    CHOICE_STATUS = [(ACTIVE, "active"), (DEACTIVED, "deactived")]

    poll_status = models.CharField(
        "poll status", max_length=10, choices=CHOICE_STATUS, default=ACTIVE, null=True
    )

    poll_name = models.CharField("pool name", max_length=50, null=True)
    poll_description = models.CharField("description", max_length=255, null=True)
    start_date = models.DateTimeField("date/time start", null=True)
    date_finish = models.DateTimeField("date/time finish", null=True)
    questions_ids = models.CharField("questions_ids", max_length=100, null=True)


class Questions(models.Model):
    ANSWER_TYPE = [
        "one answer option",
        "several answer options",
        "answer with text",
    ]
    CHOICE_TYPE_ANSWER = [
        (ANSWER_TYPE[0], "one answer option"),
        (ANSWER_TYPE[1], "several answer options"),
        (ANSWER_TYPE[2], "answer with text"),
    ]

    answer_type = models.CharField(
        "answer type",
        max_length=150,
        null=True,
        choices=CHOICE_TYPE_ANSWER,
        default=ANSWER_TYPE[0],
    )

    question = models.CharField("question", max_length=500, null=True)
    possible_answer = models.CharField("possible answer", max_length=100, null=True)
    true_answer = models.CharField("true answer", max_length=100)


class UserAnswer(models.Model):

    poll_id = models.IntegerField("poll id")
    user_id = models.IntegerField("user id")
    answers = models.CharField("answers", max_length=255)

