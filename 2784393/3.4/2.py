from simpletk import *


class ColorViewer(TApplication):
    def __init__(self):
        TApplication.__init__(self, 'RGB-coding')
        self.position = (300, 300)
        self.size = (210, 90)

        font_text_field = ('Roboto', 12)

        self.rEdit = TEdit(self, font=font_text_field, width=5)
        self.rEdit.position = (45, 5)
        self.rEdit.text = '123'

        self.gEdit = TEdit(self, font=font_text_field, width=5)
        self.gEdit.position = (45, 30)
        self.gEdit.text = '56'

        self.bEdit = TEdit(self, font=font_text_field, width=5)
        self.bEdit.position = (45, 55)
        self.bEdit.text = '80'

        font_label = ('Roboto', 12)

        self.rLabel = TLabel(self, font=font_label, text='R = ')
        self.rLabel.position = (5, 5)

        self.gLabel = TLabel(self, font=font_label, text='G = ')
        self.gLabel.position = (5, 30)

        self.bLabel = TLabel(self, font=font_label, text='B = ')
        self.bLabel.position = (5, 55)

        font_color = ('Roboto', 16, 'bold')

        self.rgbLabel = TLabel(self, font=font_color, text='#000000', fg='navy')
        self.rgbLabel.position = (100, 5)

        self.rgbRect = TLabel(self, text='', width=15, height=3)
        self.rgbRect.position = (105, 35)

        self.gEdit.onChange = self.onChangeColor
        self.rEdit.onChange = self.onChangeColor
        self.bEdit.onChange = self.onChangeColor

    def onChangeColor(self, sender):
        color = '?'
        background_color = 'SystemButtonFace'
        try:
            r = int(self.rEdit.text)
            g = int(self.gEdit.text)
            b = int(self.bEdit.text)
            if r in range(256) and g in range(256) and b in range(256):
                color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                background_color = color
        except:
            pass
        self.rgbLabel.text = color
        self.rgbRect.background = background_color


app = ColorViewer()
app.run()
