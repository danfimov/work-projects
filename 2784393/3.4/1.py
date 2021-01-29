from simpletk import *
from tkinter.messagebox import askokcancel


def AskOnExit():
    if askokcancel('Attention!',
                   'Do you really want to close the window?'):
        app.destroy()


app = TApplication('First form')
app.resizable = (True, True)
app.minsize = (600, 300)
app.maxsize = (700, 400)
app.onCloseQuery = AskOnExit

app.Run()
