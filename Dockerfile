FROM python:3.8

WORKDIR /app/
RUN pip install poetry
ADD poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev
ADD . /app/

CMD ["uvicorn", "app:app", "--port", "80"]
