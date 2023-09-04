Github visualize:
https://chrome.google.com/webstore/detail/le-git-graph-commits-grap/joggkdfebigddmaagckekihhfncdobff/related

TAB                                                    - files from directory
стрелки ВВЕРХ и ВНИЗ                                   - command cash

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
    docker build -t "imagename:tag --no-cache=True .
    docker image ls
    docker run --name "containerName" "imagename"

#HOW TO PUSH YOUR IMAGE TO DOCKER_HUB

1) docker logout
2) docker build -t "repository":"imagename" --no-cache=True .
3) docker tag "imageid" altairvirus/nntc_1:"imagename"
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
docker kill <NAMES>/<CONTAINER ID>                                      -
docker images                                                           - see all images
docker rmi <IMAGE ID> <IMAGE ID>                                        - delete image

docker image inspect <IMAGE ID>                                         - image info
docker inspect <NAMES>/<CONTAINER ID>                                   - container info
docker stats <NAMES>/<CONTAINER ID>                                     - container statistic
docker logs -f <NAMES>/<CONTAINER ID>                                   - Runtime logs of container
docker exec -it <NAMES>/<CONTAINER ID>  /bin/bash                       - in container (interactive mode)
    ls                                                                      - explore container's file system
    cd <FOLDER>                                                             - go to folder
    env                                                                     - env variables
    exit                                                                    - exit from bash of container
    ip a                                                                    - list of container's ip
    ping <NAMES> / ip                                                       - ping to check corrections
    CTRL C                                                                  - stop command
    ps xa                                                                   - see running process
docker system prune -a --volumes                                        - delete all images

               docker run -it --rm --name test_cont -v data:/usr/tests/allureResults d6ae21db8417 /bin/bash


docker run -p 8080:80 <Image name>                                      - run with ports (sever 8080 - container 80)
docker run -e VAR_VAR=123455                                            - run with variables

docker volume create <NEW VOLUME>                                       -create volume in /var/lib/docker/volumes
docker volume rm <VOLUME NAME>                                          -delete volume in docker

                           docker run --rm -v data:/usr/tests/AllureReport IMAGE

netstat -a                                                              -running ports
docker network ls                                                       -types of networks
docker network create --driver bridge <NEW NETWORK>                     -create new network
docker network inspect <NETWORK NAME>                                   -info networks
docker network rm <NAMES>/<NETWORK ID>                                  -delete network
docker network connect <NAMES>/<NETWORK ID>  <NAMES>/<CONTAINER ID>     -connect container to network

                 docker run --name new_container --net MyNet -v data:/usr/tests/AllureReport new_image

       docker run --name new_container3 -it  --rm --net MyNet -p 414:80 -v data:/usr/tests/AllureReport test:v1 /bin/bash
       http://100.111.12.214:414/ - YOUR CONTAINER SERVICE


                                        # CI / CD

docker compose up (-d)
chown -R :gitlab-runner allaccess - назначить владельца файла
chmod 777 allaccess/scripts/ - дать всем права на файл




                                    # VIRTUAL MACHINE

1) Hyper-V -> Create Ubuntu 22.04
             ## IF BLUE SCREEN AFTER LOG IN -> allow Enhanced session mode
             ## To see network interfaces -> sudo ifconfig
2) Create USER and PASSWORD
             ## sudo -i -> password to root user. After all -> exit and exit
3) Install Docker and Git
4) Install SSH
5) Deactivate sleep. target
6) Create #External switch in Hyper-V
7) Ask DevOps make static IP for host machine (described at note)
8) Create Sharing Folder, mount....

