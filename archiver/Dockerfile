FROM python:3.9.16-alpine

ENV IN_DIR /convert/from
ENV OUT_DIR /convert/to

WORKDIR /app

RUN apk add --no-cache bash zip

COPY main.sh /app

CMD ["bash", "main.sh"]