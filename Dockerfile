FROM sanicframework/sanic:3.11-latest
WORKDIR /sanic
COPY . .
RUN apk add openssl-dev python3-dev bsd-compat-headers libffi-dev
RUN pip install --no-cache --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]
