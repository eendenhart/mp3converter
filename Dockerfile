FROM python:3.9.16-alpine

ENV MP3CONVERTER_SRC /convert/from
ENV MP3CONVERTER_DST /convert/to
ENV MP3CONVERTER_EXT .m4a

WORKDIR /app

RUN apk add --no-cache unzip ffmpeg

# download latest script
ADD https://github.com/rahulsrma26/dockers/archive/refs/heads/mp3converter.zip /app/
RUN unzip mp3converter.zip -d /tmp/
RUN rm mp3converter.zip
RUN mv /tmp/dockers-mp3converter/* /app

# for local testing
# COPY . /app

CMD ["python3", "main.py"]