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




