# django-channels

- Reiniciando e ingresando a docker
  docker run -d --name redis -p 6379:6379 redis:7.0.12
  docker restart redis
  docker exec -it redis redis-cli
  ping
  exit

- Consulta especifica
  docker exec -it redis redis-cli ping

# Configuracion correcta para produccion

docker run -d --name redis -p 6379:6379 -v $(pwd)/redis.conf:/usr/local/etc/redis/redis.conf redis:7.0.12 redis-server /usr/local/etc/redis/redis.conf

# Solo para desarrollo - Exponer redis de manera publica

docker run -d --name redis -p 6379:6379 redis:6.2
