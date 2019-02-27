#!/bin/sh
# Activate the virtual environment - this will add venv/bin to the path
source venv/bin/activate
# Run venv/bin/flask db upgrade to perform any migrations (including table creation)
flask db upgrade
# Exec venv/bin/gunicorn [opts]
# `--certfile cert.pem --keyfile key.pem`: Set the cert and private key for SSL/TLS
# `-b :5000`: Bind the server to port 5000
# `--access-logfile - --error-logfile -`: Log to standard out
# `salapp:app`: Run salapp:app
exec gunicorn --certfile cert.pem --keyfile key.pem -b :5000 --access-logfile - --error-logfile - salapp:app
