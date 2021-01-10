FROM python


RUN pip install poetry 

COPY pyproject.toml poetry.lock ./
COPY src src
COPY entrypoint.sh .

RUN chmod +x ./entrypoint.sh
RUN poetry install
RUN poetry run python poll_manager/manage.py migrate
ENTRYPOINT ["./entrypoint.sh"]