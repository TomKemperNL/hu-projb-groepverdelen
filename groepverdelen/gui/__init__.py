import tkinter

import groups
import gui.chart
import gui.team


# If you're thinking 'what weird Python is this??', it's demo-code and I'm not allowed to use classes yet:)
def create_gui(messages, command_handlers, process_message, model):
    root = tkinter.Tk()
    columns = 3

    main_frame = tkinter.Frame(root)
    main_frame.pack()
    canvas = tkinter.Canvas(main_frame)
    scrollbar = tkinter.Scrollbar(canvas, orient=tkinter.VERTICAL, command=canvas.yview)
    content_frame = tkinter.Frame(canvas)
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
                       )
    canvas.create_window((0, 0), window=content_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)
    content_frame.pack()
    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    teams_frame = tkinter.Frame(content_frame)
    teams_frame.columnconfigure(tuple(range(0, columns)), weight=1)

    index = 0
    for name, members in model.items():
        team_view = team.create_team_view(teams_frame, name, members)
        team_view.grid(row=int(index / columns), column=index % columns, sticky='NSEW')
        index = index + 1

    teams_frame.pack()

    controls_frame = tkinter.Frame(content_frame)

    selected = tkinter.StringVar(controls_frame)
    team_names = list(model.keys())
    selected.set(team_names[0])

    team_label = tkinter.Label(controls_frame, text='Team')
    dropdown = tkinter.OptionMenu(controls_frame, selected, *team_names)
    name_label = tkinter.Label(controls_frame, text='Naam')
    name_field = tkinter.Entry(controls_frame)

    for c in [team_label, dropdown, name_label, name_field]:
        c.pack(side=tkinter.LEFT)

    slider_frame = tkinter.Frame(content_frame)
    for program in range(0, len(groups.PROGRAM_NAMES)):
        scale = tkinter.Scale(slider_frame, from_=1, to=len(groups.VALUES), orient=tkinter.HORIZONTAL, showvalue=False)
        scale.pack()

    controls_frame.pack()
    slider_frame.pack()

    def process_messages():
        if len(messages) > 0:
            message, arguments = messages.pop()
            process_message(message, arguments)
        root.after(100, process_messages)

    def start():
        root.after(100, process_messages)
        root.mainloop()

    return {
        'start': start
    }
