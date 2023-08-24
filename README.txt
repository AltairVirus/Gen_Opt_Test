Github visualize:
https://chrome.google.com/webstore/detail/le-git-graph-commits-grap/joggkdfebigddmaagckekihhfncdobff/related

UPDATE PIP:
    python.exe -m pip install --upgrade

INSTALL NEW LIB:
    pip3 install "libname"

UPDATE LIST OF NECESSARY LIBS:
    pip3 freeze > requirements.txt

PYTEST:
    pytest APITests --alluredir=AllureReport

CREATE ALLURE REPORT:
    allure serve AllureReport

DOCKER:
    docker build -t "imagename" --no-cache=True .
    docker image ls
    docker run --name "containerName" "imagename"

#HOW TO PUSH YOUR IMAGE TO DOCKER_HUB

1) docker logout
2) docker build -t "imagename" --no-cache=True .
3) docker tag "imagename" altairvirus/nntc_1:"imagename"
4) docker login
    #altairvirus
    #Hizmetlik1
5) docker push altairvirus/nntc_1:"imagename"


#DOCKER COMMAND

docker pull <Image name>: version                                       - upload image to local Regestry
docker run --rm -d --name MyContName <Image name> / sleep 5 / echo "I run <Image name>"   - create container and run
docker start <NAMES>/<CONTAINER ID>                                     - start container
docker ps                                                               - see running process
docker ps -a                                                            - see all containers
docker volume ls                                                        - see all volumes
docker rm <NAMES>/<CONTAINER ID>                                        - delete container
docker images                                                           - see all images
docker rmi <IMAGE ID> <IMAGE ID>                                        - delete image

docker inspect <NAMES>/<CONTAINER ID>                                   - container info
docker stats <NAMES>/<CONTAINER ID>                                     - container statistic
docker logs -f <NAMES>/<CONTAINER ID>                                   - Runtime logs of container
docker exec -it <NAMES>/<CONTAINER ID>  /bin/bash                       - in container
env                                                                     - env variables
docker system prune -a --volumes                                        - delete all images


docker run -p 8080:80 <Image name>                                      - run with ports (sever 8080 - container 80)
docker run -e VAR_VAR=123455                                            - run with variables

docker volume create <NEW VOLUME>                                       -create volume in /var/lib/docker/volumes
docker volume rm <VOLUME NAME>                                          -delete volume in docker

                           docker run --rm -v data:/usr/tests/allureResults IMAGE

netstat - a                                                             -ports
docker network ls                                                       -types of networks
docker network create --driver bridge <NEW NETWORK>                     -create new network
docker network inspect <NETWORK NAME>                                   -info networks
docker network rm <NAMES>/<NETWORK ID>