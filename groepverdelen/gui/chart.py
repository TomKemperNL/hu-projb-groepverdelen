import tkinter
from groups import PROGRAMS
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

COLORS = dict([(key, color) for key, _, color in PROGRAMS.values()])
COLORS['NONE'] = '#eeeeee'


def create_chart(parent, data):
    labels = []
    values = []
    colors = []

    for name, value in data.items():
        if value > 0:
            labels.append(name)
            values.append(value)
            colors.append(COLORS[name])

    fig = plt.figure(figsize=(2.5, 2.5))

    plt.pie(values, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    canvas = FigureCanvasTkAgg(fig, master=parent)  # A tk.DrawingArea.
    canvas.draw()
    plt.close(fig)  # currently we're refreshing by recreating everything
    # thats probably not very clever... so the alternative is -not- closing and updating here
    return canvas.get_tk_widget()
