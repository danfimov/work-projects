# пользовательский класс исключений, наследуемый от базового класса Exception
class ExperienceException(Exception):
    def __init__(self, text='Без опыта работы не нанимаем!'):
        self.txt = text
