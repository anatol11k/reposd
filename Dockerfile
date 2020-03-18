FROM python:2


WORKDIR /usr/src/app

COPY requirements.txt ./
COPY got_metrics.py /usr/src/app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT ["python", "got_metrics.py"]
