# django-channels

- Reiniciando e ingresando a docker
  docker run -d --name redis -p 6379:6379 redis:7.0.12
  docker restart redis
  docker exec -it redis redis-cli
  ping
  exit

- Consulta especifica
  docker exec -it redis redis-cli ping

# Solo para desarrollo

docker run -d --name redis -p 6379:6379 redis:6.2
