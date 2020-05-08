import tkinter as tk
import gui


def main():
    root = tk.Tk()
    gui.Window(root)
    root.resizable(False, False)
    root.title('PathFinder')
    root.mainloop()


main()
