import tkinter
from gui.chart import create_chart
import groups
from messages import REMOVE_STUDENT


def create_student_name(parent, messages, name):
    member_label = tkinter.Label(parent, text=f'- {name}', cursor='pirate')
    member_label.pack()
    member_label.bind('<Button-1>', lambda e: messages.append((REMOVE_STUDENT, name)))


def create_team_view(parent, messages, team_name, members):
    frame = tkinter.Frame(parent)
    titel = tkinter.Label(frame, text=f'{team_name}')
    titel.grid(columnspan=2)

    distribution = groups.get_team_distribution(members)
    pie = create_chart(frame, distribution)
    pie.grid(row=1, column=0)

    members_frame = tkinter.Frame(frame)
    for student in members:
        create_student_name(members_frame, messages, student['name'])

    if len(members) < 4:
        too_few = tkinter.Label(members_frame, text=f'{len(members)} leden, minstens 4', fg='red')
        too_few.pack()

    if len(members) > 5:
        too_many = tkinter.Label(members_frame, text=f'{len(members)} leden, max 5', fg='red')
        too_many.pack()

    programs_in_distribution = [key for key, value in distribution.items() if value > 0]
    missing_programs = set(groups.PROGRAM_NAMES).difference(programs_in_distribution)
    for program in missing_programs:
        missing_label = tkinter.Label(members_frame, text=f'Geen {program} in team', fg='red')
        missing_label.pack()

    members_frame.grid(row=1, column=1)

    return frame
