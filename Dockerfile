FROM python:3.11-alpine
WORKDIR /sanic
COPY . .
RUN apk update
RUN apk add openssl-dev python3-dev
RUN apk add --no-cache --update build-base \
        ca-certificates \
        openssl
RUN update-ca-certificates
RUN rm -rf /var/cache/apk/*
RUN pip install --no-cache --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]
