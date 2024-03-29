from simpletk import *


class TFloatEdit(TEdit):
    def __init__(self, parent, **kw):
        TEdit.__init__(self, parent, **kw)
        self.__value = 0
        self.onValidate = self.__validate

    def __setValue(self, value):
        self.text = str(value)

    def __validate(self):
        try:
            new_value = float(self.text)
            self.__value = new_value
            return True
        except:
            return False

    value = property(lambda x: x.__value, __setValue)


def onNumChange(sender):
    binLabel.text = 'миль = {:.3f} км'.format(sender.value / 1.852)


app = TApplication('Miles to km')

app.size = (400, 80)
app.minsize = (400, 80)
app.resizable = (True, False)
app.position = (200, 200)

f = ('Roboto', 14, 'bold')

decEdit = TFloatEdit(app, width=12, font=f)
decEdit.position = (5, 5)
decEdit.text = '1.9'

binLabel = TLabel(app, text='?', font=f, fg='navy')
binLabel.position = (155, 5)

decEdit.onChange = onNumChange

app.Run()
