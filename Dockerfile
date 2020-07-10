FROM alpine:latest

   
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip && pip3 install --no-cache --upgrade pip setuptools

WORKDIR /digitaloceanspaces

COPY . /digitaloceanspaces

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python3", "manage.py", "runserver"]
