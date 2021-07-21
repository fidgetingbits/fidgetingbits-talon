#!/usr/bin/env python
# simple Unix Domain Server (UDS) for testing json stream

import json
import os
import socket
import sys
import threading

from talon import app


class Server:
    def __init__(self):
        self.server_address = "/home/aa/.config/polybar/scripts/talonbar/uds_socket"
        self.client_list = []

        # ensure socket isn't already in use
        try:
            os.unlink(self.server_address)
        except OSError:
            if os.path.exists(self.server_address):
                raise

        self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Bind socket to port
        print("Starting server on %s" % self.server_address, file=sys.stderr)

        self.server_socket.bind(self.server_address)

        # Listen for incoming connections
        self.server_socket.listen(1)

        t1 = threading.Thread(target=self.accept_connections)
        t1.start()

    def accept_connections(self):
        while True:
            connection, client_address = self.server_socket.accept()
            self.client_list.append(connection)

            print("got a connection")
            # information every client should get no matter what
            self.send_version()

    def send_version(self):
        self.send({"version": app.version})

    def send_command(self, command):
        self.send({"command": command})

    def send(self, data):
        t2 = threading.Thread(target=self._send_to_clients, args=(data))
        t2.start()

    def _send_to_clients(self, data):
        if len(self.client_list) > 0:
            for connection in self.client_list:
                try:
                    connection.sendall(json.dumps(data).encode("utf-8"))
                except Exception:
                    # Clean up the connection
                    connection.close()
                    self.client_list[:] = [
                        x for x in self.client_list if not connection
                    ]


# XXX - eventually that's will be replaced with a built-in talon json thing
# global uds_server
# uds_server = None
# uds_server = Server()
