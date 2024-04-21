FROM python:3.11.8

# USER root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip


RUN apt-get update && apt-get install -y \
#     python3-pip \
    chromium \
    chromium-driver

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system

COPY . .

CMD ["sh", "-c", "python -m bot"]
