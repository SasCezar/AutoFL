FROM python:3.10 as python-base
RUN mkdir autofl
WORKDIR  /autofl
COPY pyproject.toml /autofl
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi
COPY . .
ENV PYTHONPATH=/autofl/src
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "api.main:app", "--bind", "0.0.0.0:8000"]