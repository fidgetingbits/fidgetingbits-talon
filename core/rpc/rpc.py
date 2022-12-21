# import tornado
# import tornado_msgpack
#
# port = 18080
#
## dispatcher
# dispatcher = tornado_msgpack.Dispatcher()
#
#
# def add(a, b):
#    return a + b
#
#
# dispatcher.add_handler("add", add)
#
# server
# server_loop = tornado.ioloop.IOLoop()
# server = tornado_msgpack.Server(server_loop, dispatcher.on_message)
# server.listen(port)

# blocking...
# server_loop.start()
