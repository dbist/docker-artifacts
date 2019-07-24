# Inspired by tutorial in https://docs.docker.com/compose/gettingstarted/
# requires:
 - dbist/apache-phoenix-pqs:4.14.2


#### creating a cluster as per [1](https://docs.docker.com/get-started/part4/)
```
docker-machine create --driver virtualbox --virtualbox-memory "4096" myvm1
docker-machine create --driver virtualbox --virtualbox-memory "1024" myvm2
```
