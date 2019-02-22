mysqlrootpw=$(docker logs mysql 2>&1 | grep GENERATED | awk '{ print $5 }')
echo "Logging in with pw: $mysqlrootpw"
docker exec -it mysql mysql -uroot -p$mysqlrootpw
