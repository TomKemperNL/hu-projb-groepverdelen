import threading

from groups import *
from messages import INCREMENT
from gui import create_gui
from web import create_web

messages = []
handlers = {}

model = initial_groups()
dummy_data(model)


def process_message(message, arguments):
    pass


gui = create_gui(messages, handlers, process_message, model)
web = create_web(messages, handlers)

if __name__ == '__main__':
    threading.Thread(target=web['start']).start()
    gui['start']()
