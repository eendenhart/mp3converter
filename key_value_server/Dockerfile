FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY main.py /app/

CMD ["python", "main.py"]
