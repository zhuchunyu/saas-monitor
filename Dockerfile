FROM python:3.7

WORKDIR /app

MAINTAINER zhuchunyu <zhuchunyu@cloud-star.com.cn>

COPY . /app
ADD pip.conf /root/.pip/pip.conf

RUN pip install -r requirements.txt

EXPOSE 5025

CMD python web.py
