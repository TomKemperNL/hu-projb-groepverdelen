import tkinter
from groups import PROGRAMS
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

COLORS = dict([(key, color) for key, _, color in PROGRAMS.values()])
COLORS['NONE'] = '#ffffff'


def create_chart(parent, data):
    labels = []
    values = []
    colors = []

    for name, value in data.items():
        labels.append(name)
        values.append(value)
        colors.append(COLORS[name])

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, autopct='%1.0f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    canvas = FigureCanvasTkAgg(fig, master=parent)  # A tk.DrawingArea.
    canvas.draw()

    return canvas.get_tk_widget()
