from unittest import TestCase
import pytest
from main import check_auth, solve, discriminant, solution


def test_successful_data():
    assert check_auth('admin', 'password') == 'Добро пожаловать'

@pytest.mark.parametrize(
    'a, b, expected',
    (
        ('user', 'password', 'Доступ ограничен'),
        ('admin', '123', 'Доступ ограничен'),
        ('maks', 'password', 'Доступ ограничен')


    )
)
def test_check_with_params(a,b,expected):
    assert check_auth(a, b) == expected



@pytest.mark.parametrize(
    'lst, workday, expected',
    (
            ([
    ["Разобрать почту", 1],
    ["Обзвонить клиентов", 2],
    ["Прочитать документацию", 1.5],
    ["Сделать отчёт", 2.5]
],8, 1.0),
            ([
    ["Задача 1", 2],
    ["Задача 2", 3],
    ["Задача 3", 3]
], 8, 0.0),
            ([], 8, 8.0),
            ([
    ["Задача 1", 4],
    ["Задача 2", 5]
],8, -1.0)
    )
)
def test_solve_with_params(lst, workday, expected):
    assert solve(lst, workday) == expected



@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        (1, -3, 2, (2.0, 1.0)),
        (1, 2, 1, -1.0),
        (1, 0, 1, "корней нет")
    )
)
def test_check_discriminant_solution_with_params(a, b, c, expected):
    assert solution(a, b, c) == expected