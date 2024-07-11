FROM python:alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip --no-warn-script-location
RUN pip install -r requirements.txt --no-cache-dir --no-warn-script-location

COPY . .