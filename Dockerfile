FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

COPY ./entrypoint.sh ./

CMD /bin/bash entrypoint.sh

