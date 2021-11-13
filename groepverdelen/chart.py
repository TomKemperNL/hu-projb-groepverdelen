import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


def create_chart(parent, data):
    labels = []
    values = []

    for name, value in data:
        labels.append(name)
        values.append(value)

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    canvas = FigureCanvasTkAgg(fig, master=parent)  # A tk.DrawingArea.
    canvas.draw()

    return canvas.get_tk_widget()
