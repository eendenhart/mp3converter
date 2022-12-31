FROM python:3.9.16-alpine

ENV MP3CONVERTER_SRC /convert/from
ENV MP3CONVERTER_DST /convert/to
ENV MP3CONVERTER_EXT .m4a

WORKDIR /app

RUN apk add  --no-cache ffmpeg

# download latest script
ADD https://raw.githubusercontent.com/rahulsrma26/dockers/master/mp3converter/main.py /app/main.py
# for local testing
# COPY . /app

CMD ["python3", "main.py"]