from simpletk import *


class THexEdit(TEdit):
    def __init__(self, parent, **kw):
        TEdit.__init__(self, parent, **kw)
        self.__value = 0
        self.onValidate = self.__validate

    def __setValue(self, value):
        self.text = str(value)

    def __validate(self):
        try:
            new_value = int(self.text, 16)
            self.__value = self.text
            return True
        except:
            return False

    value = property(lambda x: x.__value, __setValue)


app = TApplication('Hex')
app.size = (200, 80)
app.minsize = (200, 80)
app.resizable = (True, False)
app.position = (200, 200)

f = ('Roboto', 14, 'bold')

hexEdit = THexEdit(app, width=12, font=f)
hexEdit.alight = 'center'
hexEdit.position = (30, 5)
hexEdit.text = '101'

app.Run()
