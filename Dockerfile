FROM python:3.11.4

WORKDIR /app

COPY . /app


RUN pip install -r dependences.txt

EXPOSE 8000
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000", "--reload"]



