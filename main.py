import tkinter
from bottle import route, run, template
import threading
from messages import INCREMENT

root = tkinter.Tk()

counter = 0
label = tkinter.Label(root, text=f'{counter}')
label.pack()


def increment():
    global counter
    counter = counter + 1
    label.configure(text=f'{counter}')


@route('/hello/<name>')
def index(name):
    print('ooowkee1')
    messages.append(('INCREMENT',))
    print('ooowkee2')
    return template('<b>Hello {{name}}</b>!', name=name)


increment_button = tkinter.Button(root, text='+', command=increment)
increment_button.pack()

messages = []


def process_messages():
    if len(messages) > 0:
        message, arguments = messages.pop()
        if message == INCREMENT:
            increment()
    root.after(100, process_messages)


if __name__ == '__main__':
    threading.Thread(target=lambda: run(host='localhost', port=8080)).start()
    root.after(100, process_messages)
    root.mainloop()
