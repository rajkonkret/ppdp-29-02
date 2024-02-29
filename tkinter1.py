import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Wartość")
        self.label2 = tkinter.Label(self.main_window, text="Radek")
        self.label3 = tkinter.Label(self.main_window, text="Python")
        self.label4 = tkinter.Label(self.main_window, text="Test")

        self.label1.pack(side="left")
        self.label2.pack(side="right")
        self.label3.pack(side="top")
        self.label4.pack(side="bottom")

        tkinter.mainloop()


my_gui = MyGui()
