FROM ubuntu
RUN apt-get update -y
RUN apt-get install python3 -y
# RUN apt-get install python3-pip -y

COPY test_data.csv /app/test_data.csv
COPY logtojson.py /app/logtojson.py
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt
CMD ["python3", "/app/logtojson.py"]
# ENTRYPOINT ["python3"]
