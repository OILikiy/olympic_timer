# Olympic_timer

A small example of a project that shows the remaining time until the Olympic Games using Flask and Docker.

## Usage
### run the image:
docker run -p 5000:5000 olympic-timer
### insert in web browser this address:
http://localhost:8888
### commands that show running image
docker ps
### commands that show stopped image
docker ps -a
### output after docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
### stopping
docker stop CONTAINER ID
### remove from processing
docker rm CONTAINER ID
