import tkinter
import tkinter.messagebox
import groups
from messages import ADD_STUDENT


def create_slide(parent, i, program_name):
    scale_label = tkinter.Label(parent, text=f'{program_name}')
    value = tkinter.IntVar(parent)
    value_label = tkinter.Label(parent, text='0')

    scale = tkinter.Scale(parent,
                          from_=1, to=len(groups.VALUES), variable=value,
                          command=lambda x: value_label.configure(text=f'{groups.VALUES[int(x) - 1]}'),
                          orient=tkinter.HORIZONTAL, showvalue=False)
    scale_label.grid(column=0, row=i)
    scale.grid(column=1, row=i)
    value_label.grid(column=2, row=i)
    return value


def create_add_student(parent, messages, team_names):
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
    choices = {}
    for i in range(0, len(groups.PROGRAM_NAMES)):
        program_name = groups.PROGRAM_NAMES[i]
        choices[program_name] = create_slide(slider_frame, i, program_name)

    controls_frame.pack()
    slider_frame.pack()

    def add_student():
        name = name_field.get()
        team = selected.get()
        tupled_choice = [(program, groups.VALUES[value.get() - 1]) for program, value in choices.items()]

        if groups.is_valid_groupchoice(tupled_choice):
            messages.append((ADD_STUDENT, (team, name, tupled_choice)))
        else:
            tkinter.messagebox.showerror('Ongeldige keuze', 'Geen geldige richting keuzen (totaal 100)')

    submit_button = tkinter.Button(parent, text='Ok', command=add_student)
    submit_button.pack()

    return controls_frame
