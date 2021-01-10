def poll_questions(model_name, questions_ids):
    questions = questions_ids.split(";")

    question_dict = {}
    question_number = 1
    for question_id in questions:
        question = model_name.objects.filter(id=question_id)
        question = question.values()[0]
        question.pop("true_answer", None)
        question_dict[f"{question_number}"] = question
        question_number += 1

    return question_dict
