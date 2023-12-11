tag: user.docker
-

# NOTE: Keep this file in sync with docker_sudo.talon
# Due to cases were you use podman, and it is aliased to docker, you won't want to be adding sudo, as it may result in
# podman not actually running.
#
# The alternative approach would be to implement every command in python, and
# check the tag to see if the user wants sudo prefix, but that seems annoying atm

#docker: "docker "
docker build:
    insert("docker build .")
    key("enter")
docker build (tag | tagged): user.insert_between('docker build -t ", " .')
docker pull: "docker pull "
docker kill: "docker kill "
docker kill all: "docker stop $(docker ps -a -q)\n"
docker run: "docker run -d "
docker run interactive: "docker run -it --rm "
docker (log | logs): "docker logs "
docker inspect: "docker inspect "
docker enter: "~/bin/docker-enter "
docker (terminal | shell):
    insert("docker ps\n")
    user.insert_cursor("docker exec -it [|] /bin/bash")

# images
docker (image | images) list: insert("docker images\n")
docker image prune: insert("docker image prune\n")
docker image prune label: insert("docker image prune --filter label=")
docker image remove: insert("docker image rm ")
docker image inspect:
    insert("docker images\n")
    insert("docker image inspect ")
docker image build: insert("docker image build ")
docker image label: insert("docker images -f label=")
docker image label <user.text>: insert("docker images -f label={text}\n")

# containers
docker [container] prune: insert("docker container prune ")
docker [container] list all: insert("docker ps -a\n")
docker [container] list: insert("docker ps\n")
docker [container] remove: insert("docker rm ")
docker [container] remove all: insert("docker rm $(docker ps -a -q)\n")
docker [container] remove and kill all:
    insert("docker stop $(docker ps -a -q)\n")
    insert("docker rm $(docker ps -a -q)\n")

docker [container] stop: "docker stop "
docker [container] copy: insert("docker cp ")
docker [container] inspect:
    insert("docker ps\n")
    insert("docker inspect ")
docker [container] attach:
    insert("docker ps\n")
    insert("docker attach ")

# volumes
docker volume list: insert("docker volume ls\n")
docker volume create: insert("docker volume create ")
docker volume inspect: insert("docker volume inspect ")
docker volume remove: insert("docker volume rm ")

# system
docker system prune: insert("docker system prune")
docker system prune all: insert("docker system prune -a")

## docker Compose
docker compose up: "docker-compose up\n"
docker compose start: "docker-compose start\n"
docker compose stop: "docker-compose stop\n"
docker compose build: "docker-compose build\n"
docker compose kill: "docker-compose kill\n"

# docker visualization (requires dockviz)
docker image tree: "dockviz images -t\n"
docker image incremental tree: "dockviz images -t -i\n"
docker image labeled tree: "dockviz images -t -l\n"
