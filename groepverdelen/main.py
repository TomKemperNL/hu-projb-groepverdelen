import threading

import groups
from groups import *
from messages import ADD_STUDENT
from gui import create_gui
from web import create_web

messages = []
handlers = {}

model = initial_groups()
dummy_data(model)


# The tricky part here is that Bottle works in a different thread.
# And TKinter does not like it when you change the UI from a different thread...
def process_message(message, arguments):
    if message == ADD_STUDENT:
        groups.add_student_choice(model, *arguments)
        gui['refresh_charts']()


gui = create_gui(messages, handlers, process_message, model)
web = create_web(messages, handlers)

if __name__ == '__main__':
    threading.Thread(target=web['start']).start()
    gui['start']()
