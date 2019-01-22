FROM python:3.7

WORKDIR /app

MAINTAINER zhuchunyu <zhuchunyu@cloud-star.com.cn>

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5025

CMD python web.py
