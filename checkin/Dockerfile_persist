# syntax=docker/dockerfile:1
FROM python
WORKDIR /app
COPY . .
RUN pip3 install flask
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
