FROM python:3.7-alpine

# Create salapp user in container
RUN adduser -D salapp
# Set workdir for container
WORKDIR /home/salapp
# Copy requirements into WORKDIR in container
COPY requirements.txt requirements.txt
# Create virtual environment in venv
RUN python -m venv venv
# Install requirements into venv
RUN venv/bin/pip install -r requirements.txt
# Install deployment requirements
RUN venv/bin/pip install gunicorn pymysql
# Copy app, deployment, and cert/key files into the container WORKDIR
COPY app app
COPY migrations migrations
COPY salapp.py boot.sh ./
COPY cert.pem key.pem ./
# Make boot.sh executable
RUN chmod a+x boot.sh
# Set the FLASK_APP environment variable to be constant "salapp.py"
ENV FLASK_APP salapp.py
# Change ownership of everything, recursively, WORKDIR downwards to salapp:salapp
RUN chown -R salapp:salapp ./
# Become the salapp user added earlier
USER salapp
# Expose port 5000 from the container
EXPOSE 5000
# Set the entrypoint script to boot.sh
ENTRYPOINT ["./boot.sh"]
