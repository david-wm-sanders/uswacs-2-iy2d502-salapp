FROM python:3.7-alpine

# Create salapp user in container
RUN adduser -D salapp

# Set workdir for container
WORKDIR /home/salapp

# Copy requirements from local dir to WORKDIR
COPY requirements.txt requirements.txt
# Create virtual environment in venv
RUN python -m venv venv
# Install requirements into venv
RUN venv/bin/pip install -r requirements.txt
# Install deployment requirements
RUN venv/bin/pip install gunicorn pymysql

# Copy app from local dir to WORKDIR
COPY app app
COPY migrations migrations
COPY salapp.py boot.sh ./
# Make boot.sh executable
RUN chmod a+x boot.sh

ENV FLASK_APP salapp.py

RUN chown -R salapp:salapp ./
USER salapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
