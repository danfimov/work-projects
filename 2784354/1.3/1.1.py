month_number= int(input())
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 < month_number < 13:
    print(days_in_months[month_number-1])
else:
    raise ValueError('Некрорректный номер месяца')