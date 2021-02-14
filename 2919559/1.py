list_books = list(input().split(', '))  # считываем все названия книг
list_numbers = list(input().split(', '))  # считываем все номера книг
your_books = list(input().split(', '))  # считываем все названия книг у Жени

for i in range(len(list_books)):  # идем по индексам из списка книг
    if list_books[i] not in your_books:  # если книга не встречается в списке книжек Жени...
        print(list_numbers[i])  # ...то выписываем её номер
