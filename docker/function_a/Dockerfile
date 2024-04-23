FROM python:3.11

# intended to run via Keda - topic: FUNCTION_A

ENV PYTHONUNBUFFERED True

COPY ../../requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ../.. ./

CMD ["python", "./functions.service_a.py"]
