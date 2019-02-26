docker run --name salapp -d -p 80:5000 -p 443:5000 --rm -e FLASK_ENV=development -e SECRET_KEY=$1 -e RECAPTCHA_PUBLIC_KEY=$2 -e RECAPTCHA_PRIVATE_KEY=$3  --link mysql:dbserver -e DATABASE_URI=mysql+pymysql://salapp:debugpw54321@dbserver/salapp salapp:latest
