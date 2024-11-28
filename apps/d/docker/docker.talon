tag: user.docker
tag: user.podman
app: terminal
-

docker build: user.docker("build .\n")
docker build (tag | tagged):
    user.docker("build -t ")
    user.insert_between("", " .")
docker pull: user.docker("pull ")
docker kill:
    user.docker("ps\n")
    user.docker("kill ")
docker kill all:
    user.docker("stop $(")
    user.docker("ps -a -q)\n")
docker run: user.docker("run -d ")
docker run interactive: user.docker("run -it --rm ")
docker (log | logs): user.docker("logs ")
docker inspect: user.docker("inspect ")
docker (terminal | shell):
    user.docker("ps\n")
    user.docker("exec -it ")
    user.insert_between("", " /bin/sh")

# images
docker (image | images) list: user.docker("images\n")
docker image prune: user.docker("image prune\n")
docker image prune label: user.docker("image prune --filter label=")
docker image remove: user.docker("image rm ")
docker image inspect:
    user.docker("images\n")
    user.docker("image inspect ")
docker image build: user.docker("image build ")
docker image label: user.docker("images -f label=")
docker image label <user.text>: user.docker("images -f label={text}\n")

# containers
docker [container] prune: user.docker("container prune ")
docker [container] list all: user.docker("ps -a\n")
docker [container] list: user.docker("ps\n")
docker [container] remove: user.docker("rm ")
docker [container] remove all: user.docker("rm $(docker ps -a -q)\n")
docker [container] remove and kill all:
    user.docker("stop $(docker ps -a -q)\n")
    user.docker("rm $(docker ps -a -q)\n")

docker [container] stop: user.docker("stop ")
docker [container] copy: user.docker("cp ")
docker [container] inspect:
    user.docker("ps\n")
    user.docker("inspect ")
docker [container] attach:
    user.docker("ps\n")
    user.docker("attach ")

# volumes
docker volume list: user.docker("volume ls\n")
docker volume create: user.docker("volume create ")
docker volume inspect: user.docker("volume inspect ")
docker volume remove: user.docker("volume rm ")

# system
docker system prune: user.docker("system prune")
docker system prune all: user.docker("system prune -a")

## docker Compose
docker compose up: user.docker_compose("up\n")
docker compose start: user.docker_compose("start\n")
docker compose stop: user.docker_compose("stop\n")
docker compose build: user.docker_compose("build\n")
docker compose kill: user.docker_compose("kill\n")

# docker visualization (requires dockviz)
docker image tree: user.docker_viz("images -t\n")
docker image incremental tree: user.docker_viz("images -t -i\n")
docker image labeled tree: user.docker_viz("images -t -l\n")
