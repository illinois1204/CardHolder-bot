FROM python:3.12.8-alpine3.20

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && \
    mkdir -p storage/any storage/defined

CMD ["python", "-m", "bot.main"]
