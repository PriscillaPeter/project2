# Import necessary modules to create our calculator using Tkinter
from tkinter import Tk
from tkinter import *
from math import *


# The Calculator class host the full functionality of our program i.e every vari
class Calculator():
    # Section 1: initializes the GUI, names the GUI, adds background color
    def __init__(self, gui):

        self.gui = gui
        self.string = StringVar()
        entry = Entry(self.gui, textvariable=self.string)
        entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
        entry.configure(background='#c8d0e7')
        entry.focus()

        # Section 2: Buttons that will appear on our calculator
        calc_inputs = [
            '7', '8', '9', '/', '%', 'delete', 'clear', '4', '5', '6', '*', '(', ')',
            '**', '1', '2', '3', '-', '=', ',', '0', '.', '+', 'min', 'pow', 'log10',
            'sin', 'cos', 'tan()', 'max', 'π', 'degrees', 'radians'
        ]
        # styling for value, count, row and col variables are the specifics need for grid positioning
        current_value = 1
        position = 0
        row = 1
        col = 0
        # stying for regular number blocks and
        for current_value in calc_inputs:
            padx = 10
            pady = 10
            if (position == 7):
                row = 2
                col = 0
            if (position == 14):
                row = 3
                col = 0
            if (position == 19):
                row = 4
                col = 0
            if (position == 26):
                row = 5
                col = 0
            if (position == 33):
                row = 6
                col = 0
            if (current_value == '='):

                # styles and positions for the equal, delete, clear and addchar buttons
                buttons = Button(
                    self.gui,
                    height=2,
                    width=4,
                    padx=70,
                    pady=pady,
                    text=current_value,
                    command=lambda current_value=current_value: self.equals())
                buttons.grid(row=row, column=col, columnspan=3, padx=2, pady=2)
                buttons.configure(background='#6d5dfc')

            elif (current_value == 'delete'):  # delete's one character at a time
                buttons = Button(
                    self.gui,
                    height=2,
                    width=4,
                    padx=padx,
                    pady=pady,
                    text=current_value,
                    command=lambda current_value=current_value: self.delete())
                buttons.grid(row=row, column=col, padx=1, pady=1)
                buttons.configure(background='#8abdff')
            elif (current_value == 'clear'):  # clears the entire data area
                buttons = Button(
                    self.gui,
                    height=2,
                    width=4,
                    padx=padx,
                    pady=pady,
                    text=current_value,
                    command=lambda current_value=current_value: self.clearall())
                buttons.grid(row=row, column=col, padx=1, pady=1)
                buttons.configure(background='#8abdff')
            else:
                buttons = Button(gui,
                                 height=2,
                                 width=4,
                                 padx=padx,
                                 pady=pady,
                                 text=current_value,
                                 command=lambda current_value=current_value: self.
                                 addChar(current_value))
                buttons.grid(row=row, column=col, padx=1, pady=1)
                buttons.configure(background='#9baacf')

            col = col + 1
            position = position + 1

    def clearall(self) -> None:  # wipes clear the entire data field
        self.string.set('')

    def equals(self):
        result = ""

        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "invalid"
        self.string.set(result)

    def addChar(self, char) -> None:
        self.string.set(self.string.get() + (str(char)))

    def delete(self) -> None:
        self.string.set(self.string.get()[0:-1])
