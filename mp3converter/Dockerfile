FROM python:3.9.16-alpine

ENV MP3CONVERTER_SRC /convert/from
ENV MP3CONVERTER_DST /convert/to
ENV MP3CONVERTER_EXT .m4a

WORKDIR /app

RUN apk add --no-cache unzip ffmpeg

COPY main.py /app

CMD ["python3", "main.py"]