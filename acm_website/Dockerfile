# syntax=docker/dockerfile:1

FROM python

RUN mkdir /app

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python3", "-m", "http.server"]
