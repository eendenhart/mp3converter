FROM python:3.9.16-alpine

ENV IN_DIR /convert/from
ENV OUT_DIR /convert/to
ENV IMPORT_DIR /import/gpg
ENV EMAIL test@abc.com

WORKDIR /app

RUN apk add --no-cache zip gnupg

COPY main.sh /app

CMD ["sh", "main.sh"]