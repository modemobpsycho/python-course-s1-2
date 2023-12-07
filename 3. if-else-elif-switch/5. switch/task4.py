# Получите номер месяца от пользователя
month_number = int(input())
# Используйте оператор match-case для определения количества дней в месяце
match month_number:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31")
    case 4 | 6 | 9 | 11:
        print("30")
    case 2:
        print("28")
