FROM python:3.9.16-slim

ENV SRC /convert/from
ENV DST /convert/to

WORKDIR /app

RUN  apt-get update && apt-get install -y 'wget' 'ffmpeg'

# download latest script
RUN wget -O main.py 'https://raw.githubusercontent.com/rahulsrma26/dockers/master/mp3converter/main.py'

CMD ["python3", "main.py", "echo ${SRC}", "echo ${DST}"]