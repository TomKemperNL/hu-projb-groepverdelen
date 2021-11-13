import threading
from messages import INCREMENT
from gui import create_gui
from web import create_web

messages = []
handlers = {}

counter = 0


def increment():
    global counter
    counter = counter + 1
    gui['set_label'](f'{counter}')


handlers['increment'] = increment


def process_message(message, arguments):
    if message == INCREMENT:
        increment()


gui = create_gui(messages, handlers, process_message)
web = create_web(messages, handlers)

if __name__ == '__main__':
    threading.Thread(target=web['start']).start()
    gui['start']()
