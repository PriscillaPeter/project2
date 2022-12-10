# imports our calculator into this our main page.
from calculator import *

# Main allows our import calculator module to be displayed and gives its parameters


def main():
    window = Tk()
    window.title('Project 2: Calculator')
    window.configure(background="#E4EBF5")
    window.geometry('800x630')
    window.resizable(False, False)

    gui = Calculator(window)
    window.mainloop()


if __name__ == '__main__':
    main()
