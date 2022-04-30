import tkinter
import main_frame2

class ClockApp(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        frame = main_frame2.MainFrame(self)
        frame.pack()

if __name__ == '__main__':
    app = ClockApp()
    app.mainloop()