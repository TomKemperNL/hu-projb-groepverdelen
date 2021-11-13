import tkinter
import chart
import groups


# If you're thinking 'what weird Python is this??', it's demo-code and I'm not allowed to use classes yet:)
def create_gui(messages, command_handlers, process_message, model):
    root = tkinter.Tk()

    counter = 0
    label = tkinter.Label(root, text=f'{counter}')
    label.pack()

    for name, members in model.items():
        distribution = groups.get_team_distribution(members)
        label = tkinter.Label(root, text=f'{name}').pack()

        chart_team = chart.create_chart(root, distribution)
        chart_team.pack()

    def process_messages():
        if len(messages) > 0:
            message, arguments = messages.pop()
            process_message(message, arguments)
        root.after(100, process_messages)

    def start():
        root.after(100, process_messages)
        root.mainloop()

    return {
        'set_label': lambda tekst: label.configure(text=str(tekst)),
        'start': start
    }
