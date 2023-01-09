FROM python:3.10

RUN apt-get update

WORKDIR /usr/src/backend

COPY apis /usr/src/backend/apis
COPY apis/run.py /usr/src/backend/run.py
COPY requirements.txt /usr/src/backend/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo "building..."

ENV FLASK_APP "apis.run"
ENV FLASK_CONFIG_MODE "development"

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]


