FROM python:3.8
MAINTAINER "ahri"<ahriknow@gmail.cn>
ADD ./ /project/siban
COPY pip.conf /etc/pip.conf
WORKDIR /project/siban
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 9000
ENTRYPOINT ["gunicorn", "-w", "2", "-b", "0.0.0.0:9000", "siban.wsgi"]