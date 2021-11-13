import tkinter

import groups
import gui.chart
import gui.team
from gui.add_student import create_add_student


# If you're thinking 'what weird Python is this??', it's demo-code and I'm not allowed to use classes yet:)
def create_gui(messages, command_handlers, process_message, model):
    root = tkinter.Tk()
    root.geometry('1024x768')
    columns = 3

    canvas = tkinter.Canvas(root)
    scrollbar = tkinter.Scrollbar(canvas, orient=tkinter.VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = tkinter.Frame(canvas)

    canvas.create_window((0, 0), window=content_frame, anchor='nw')

    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    teams_frame = tkinter.Frame(content_frame)
    teams_frame.columnconfigure(tuple(range(0, columns)), weight=1)
    teams_frame.pack()

    def refresh_charts():
        for child in teams_frame.winfo_children():
            child.destroy()

        index = 0
        for name, members in model.items():
            team_view = team.create_team_view(teams_frame, messages, name, members)
            team_view.grid(row=int(index / columns), column=index % columns, sticky='NSEW')
            index = index + 1

    add_controls = create_add_student(content_frame, messages, list(model.keys()))
    add_controls.pack()

    refresh_charts()

    def process_messages():
        if len(messages) > 0:
            message, arguments = messages.pop()
            process_message(message, arguments)
        root.after(100, process_messages)

    def start():
        root.after(100, process_messages)
        root.mainloop()

    return {
        'start': start,
        'refresh_charts': refresh_charts
    }
