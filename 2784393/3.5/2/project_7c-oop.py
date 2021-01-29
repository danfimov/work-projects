from model import Calc
from simpletk import *
from tkinter.messagebox import showerror


class TCalculator(TApplication):
    def __init__(self):
        TApplication.__init__(self, "Калькулятор")
        self.size = (300, 150)

        self.Input = TComboBox(self, values=[], height=1)
        self.Input.align = "top"
        self.Input.text = "sin(1.2)*sqrt(1.7)/abs(cos(3.2))"
        self.Input.bind('<Key-Return>', self.doCalc)

        self.Answers = TListBox(self)
        self.Answers.align = "client"

    def doCalc(self, event):
        expr = self.Input.text
        try:
            x = Calc(expr)
            self.Answers.insert(0, expr + "=" + str(x))
            if not self.Input.findItem(expr):
                self.Input.addItem(expr)
        except:
            showerror("Ошибка", "Неверное выражение \n" + expr)


app = TCalculator()
app.Run()
