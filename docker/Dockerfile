FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev postgresql-client gettext

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --update bash && rm -rf /var/cache/apk/*

ADD ./ ./

RUN pip3 install -r ./requirements.txt

ADD ./docker/entrypoint.sh /project

WORKDIR /project

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
