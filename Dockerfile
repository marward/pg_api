FROM python

COPY requirements.txt /opt

RUN pip3 install -r /opt/requirements.txt 

COPY src /opt/src

WORKDIR /opt/src

CMD ["python3", "-u", "app.py"]
