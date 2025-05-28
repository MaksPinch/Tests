import unittest
from unittest import TestCase
from yandex import create_folder

class TestYdDisk(TestCase):
    def test_create_folder_with_params(self):
        for i, (name, expected) in enumerate((
                ('Test', 'Папка уже существует.'),
                ('new_yandex_folder', 'Папка успешно создана.'),
                ('another_new_yandex_folder', 'Папка успешно создана.')

        )):
            with self.subTest(i):
                result = create_folder(name)
                self.assertEqual(result, expected)


