tag: user.docker
-

#docker: "sudo docker "
docker build:
    insert("sudo docker build .")
    key("enter")
docker build (tag|tagged):
    insert("sudo docker build -t \"\" .")
    key("left:3")
docker pull: "sudo docker pull "
docker kill: "sudo docker kill "
docker kill all: "sudo docker stop $(sudo docker ps -a -q)\n"
docker run: "sudo docker run -d "
docker run interactive: "sudo docker run -it --rm "
docker (log|logs): "sudo docker logs "
docker inspect: "sudo docker inspect "
docker enter: "~/bin/docker-enter "
docker (terminal|shell):
    insert("sudo docker ps\n")
    user.insert_cursor("sudo docker exec -it [|] /bin/bash")

# images
docker (image|images) list:
    insert("sudo docker images\n")
docker image prune:
    insert("sudo docker image prune\n")
docker image prune label:
    insert("sudo docker image prune --filter label=")
docker image remove:
    insert("sudo docker image rm ")
docker image inspect:
    insert("sudo docker images\n")
    insert("sudo docker image inspect ")
docker image build:
    insert("sudo docker image build ")
docker image label:
    insert("sudo docker images -f label=")
docker image label <user.text>:
    insert("sudo docker images -f label={text}\n")


# containers
docker [container] prune:
    insert("sudo docker container prune ")
docker [container] list all:
    insert("sudo docker ps -a\n")
docker [container] list:
    insert("sudo docker ps\n")
docker [container] remove:
    insert("sudo docker rm ")
docker [container] remove all:
    insert("sudo docker rm $(sudo docker ps -a -q)\n")
docker [container] remove and kill all:
    insert("sudo docker stop $(sudo docker ps -a -q)\n")
    insert("sudo docker rm $(sudo docker ps -a -q)\n")


docker [container] stop: "sudo docker stop "
docker [container] copy:
    insert("sudo docker cp ")
docker [container] inspect:
    insert("sudo docker ps\n")
    insert("sudo docker inspect ")
docker [container] attach:
    insert("sudo docker ps\n")
    insert("sudo docker attach ")


# volumes
docker volume list:
    insert("sudo docker volume ls\n")
docker volume create:
    insert("sudo docker volume create ")
docker volume inspect:
    insert("sudo docker volume inspect ")
docker volume remove:
    insert("sudo docker volume rm ")

# system
docker system prune:
    insert("sudo docker system prune")
docker system prune all:
    insert("sudo docker system prune -a")

## docker Compose
docker compose up: "docker-compose up\n"
docker compose start: "docker-compose start\n"
docker compose stop: "docker-compose stop\n"
docker compose build: "docker-compose build\n"
docker compose kill: "docker-compose kill\n"

# docker visualization (requires dockviz)
docker image tree: "sudo dockviz images -t\n"
docker image incremental tree: "sudo dockviz images -t -i\n"
docker image labeled tree: "sudo dockviz images -t -l\n"
