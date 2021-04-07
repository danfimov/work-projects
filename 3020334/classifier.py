

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import SGDClassifier

import warnings
warnings.filterwarnings('ignore')

print('''Этот классификатор текстов способен понять,
к какой из трех тематик принадлежит текст:
астрономия, зоология или медицина.''')

print('\n---Загрузка датасета для обучения--')

#  Работа с датасетом
data = pd.read_csv('Articles N+1.csv')

df = data.drop(['AdClasses', 'Unnamed: 0'], axis=1)
df.dropna(inplace=True)
df = df[df['Class'] == 'Зоология'].append(df[df['Class'] == 'Медицина']).append(df[df['Class'] == 'Астрономия'])

print('---Обучение модели---')

#  Обучение  модели

pipe = Pipeline([('vect', CountVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('model', SGDClassifier(random_state=17))])
model = pipe.fit(df['Text'].values, df['Class'])

print('--Обучение завершено---')

#  Работа с данными от пользователя
file_name = input('\nВведите имя файла, из которого импортируется текст: ')

with open(file_name, 'r') as file:
    file_text = file.read()

prediction = model.predict([file_text])

print('\nТематика загруженного текста:', prediction[0])