month_number, day = map(int, input().split())
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 0 < month_number < 13:
    days_in_month = days_in_months[month_number - 1]
else:
    raise ValueError('Некрорректный номер месяца')

if days_in_month >= day > 0:
    print(f'Дней до Нового года: {days_in_month - day + sum(days_in_months[month_number:])}')
else:
    raise ValueError('Некрорректный номер дня в месяце')