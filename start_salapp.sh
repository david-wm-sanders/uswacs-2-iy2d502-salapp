docker stop salapp
docker rm salapp
docker run --name salapp -d -p 443:5000 -e FLASK_ENV=development -e SECRET_KEY=$1 -e RECAPTCHA_PUBLIC_KEY=$2 -e RECAPTCHA_PRIVATE_KEY=$3  --link mysql:dbserver -e DATABASE_URI=mysql+pymysql://salapp:debugpw54321@dbserver/salapp salapp:latest
