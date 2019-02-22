docker run --name salapp -p 8000:5000 --rm -e FLASK_ENV=development -e SECRET_KEY=$1 -e RECAPTCHA_PUBLIC_KEY=$2 -e RECAPTCHA_PRIVATE_KEY=$3 salapp:latest 
