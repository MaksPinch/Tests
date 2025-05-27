def check_auth(login: str, password: str):

    if login == "admin" and password == "password": # Здесь напишите свой код для проверки условии
        result = "Добро пожаловать" # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
    else:
        result =  "Доступ ограничен"# В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше

    return result



def solve(todo_list: list, workday: float = 8):
    worktime = 0.0
    for i in todo_list:# посчитайте в цикле сумму рабочего времени и сохраните в переменную worktime
        worktime += i[1]
    return round(workday - worktime, 2)



def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b**2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return "корней нет"
    elif discriminant(a,b,c) == 0:
        b1  = -b
        a1 = 2*a
        return b1 / a1
    else:
        x1 =  (-b + (discriminant(a, b, c)** 0.5)) / (2 * a)
        x2 =  (-b - (discriminant(a, b, c)** 0.5)) / (2 * a)
        return x1, x2


