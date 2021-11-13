import tkinter
import groups


def create_add_student(parent, team_names):
    controls_frame = tkinter.Frame(parent)

    input_frame = tkinter.Frame(controls_frame)
    input_frame.pack()
    selected = tkinter.StringVar(input_frame)
    selected.set(team_names[0])

    team_label = tkinter.Label(input_frame, text='Team')
    dropdown = tkinter.OptionMenu(input_frame, selected, *team_names)
    name_label = tkinter.Label(input_frame, text='Naam')
    name_field = tkinter.Entry(input_frame)

    for c in [team_label, dropdown, name_label, name_field]:
        c.pack(side=tkinter.LEFT)

    slider_frame = tkinter.Frame(parent)
    for program in range(0, len(groups.PROGRAM_NAMES)):
        scale = tkinter.Scale(slider_frame, from_=1, to=len(groups.VALUES), orient=tkinter.HORIZONTAL, showvalue=False)
        scale.pack()

    controls_frame.pack()
    slider_frame.pack()

    return controls_frame
