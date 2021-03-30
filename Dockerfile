FROM alpine:3.7

RUN apk add --no-cache python3-dev && pip3 install pip

WORKDIR /app

COPY /requirements.txt /app/requirements.txt

RUN pip install --upgrade -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["python3"]

CMD [ "mongoDB.py" ]