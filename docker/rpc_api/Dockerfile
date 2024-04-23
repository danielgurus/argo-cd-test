FROM python:3.11

# intended to run as a RPC API in k8s

ARG APP_START=main.rpc_main:app
ARG APP_PORT=8005

ENV APP_START ${APP_START}
ENV PYTHONUNBUFFERED True

ENV APP_HOME /
WORKDIR $APP_HOME
COPY ../../requirements.txt requirements.txt

ENV PORT ${APP_PORT}

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${APP_PORT}

COPY ../.. ./

CMD exec uvicorn --proxy-headers --app-dir /python/src --host 0.0.0.0 --port ${PORT} --workers 1 ${APP_START}
