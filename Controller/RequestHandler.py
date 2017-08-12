from threading import Thread
import time


class RequestHandler(Thread):

    __update = None

    def __init__(self, update):
        super(RequestHandler, self).__init__()

    def run(self):
        return None
