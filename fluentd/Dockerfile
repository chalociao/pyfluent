FROM ubuntu
RUN apt-get update -y
RUN apt-get install python3 -y
# RUN apt-get install python3-pip -y

COPY app.py /tmp/app.py
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt
CMD ["python3", "/tmp/app.py"]
