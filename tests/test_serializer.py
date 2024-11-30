import unittest
import os


def create_test_case(test_dir, expected_serial_file_name, result_serial_file_name):
    """
    Создаёт тестовую функцию для сравнения файлов в указанном тестовом каталоге.
    """
    def test_case(self):
        # Пути к файлам
        file1 = os.path.join(test_dir, f'{expected_serial_file_name}.xml')
        file2 = os.path.join(test_dir, f'{result_serial_file_name}.xml')

        # Сравниваем файлы
        with open(file1, 'r', encoding='utf-8') as file1_obj, open(file2, 'r', encoding='utf-8') as file2_obj:
            file1_lines = file1_obj.readlines()
            file2_lines = file2_obj.readlines()

        # Сравниваем количество строк
        self.assertEqual(len(file1_lines), len(file2_lines),
                         f"Файлы имеют разное количество строк: {len(file1_lines)} и {len(file2_lines)}")

        # Сравниваем построчно
        for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
            self.assertEqual(line1, line2,
                             f"Строка {i} отличается:\n\tФайл 1: {line1.strip()}\n\tФайл 2: {line2.strip()}")

    return test_case


class TestSerializer(unittest.TestCase):
    pass


# Автоматически добавляем тесты для каждого подкаталога
test_cases_dir = 'tests/test_cases'
expected_serial_file_name = 'expected_output'
result_serial_file_name = 'network_devices'

subdirectories = [
    os.path.join(test_cases_dir, d) for d in os.listdir(test_cases_dir) if os.path.isdir(os.path.join(test_cases_dir, d))
]

for subdir in subdirectories:
    test_case_name = f"test_{os.path.basename(subdir)}"
    test_func = create_test_case(subdir, expected_serial_file_name, result_serial_file_name)
    setattr(TestSerializer, test_case_name, test_func)
