FROM python:3.11.5-slim-bullseye

# setting work directory
WORKDIR /project

# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

# Copy the content of the directory into the Docker image
COPY . /project

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

#Install project dependencies
RUN pip3 install -r requirements.txt

RUN python manage.py makemigrations && python manage.py migrate 

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000

