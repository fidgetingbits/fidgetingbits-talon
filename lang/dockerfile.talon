code.language: docker
win.title: /Dockerfile/
-
# XXX - The win title thing above should get fixed because sometimes I probably
# import docker files that don't have that name
run off:
    insert("&& \\")
    key(enter)

expose <number>: "EXPOSE {number}"
