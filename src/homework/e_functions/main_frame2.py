import tkinter
import clock

class MainFrame(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        self.canvases = []
        for x in range(1):
            self.canvases.append(clock.Clock(self,
                              zone=['Central Standard Time'][x], row=0, column=x))
