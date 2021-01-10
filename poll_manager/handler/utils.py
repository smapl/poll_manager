def dict_generate(row: str):
    list_answers = row.split(";")

    if len(list_answers) > 1:
        dict_answers = {}

        for i in range(len(list_answers)):
            dict_answers[str(i + 1)] = list_answers[i]

        return dict_answers

    else:
        return {"error": "failed Poll"}
