import unittest
import os
import importlib

from src.NetworkDeviceParser import NetworkDeviceParser


def create_test_case(test_dir):
    """
    Создаёт тестовую функцию для заданного тест-кейса.
    """
    def test_case(self):

        # Инициализируем парсер
        device_parser = NetworkDeviceParser()

        # Пути к файлам
        net_dev_output_file = os.path.join(test_dir, 'network_device_output.txt')
        expected_model_module = f"{test_dir.replace('/', '.')}.expected_model"

        # Парсим файл
        network_devices_dict = device_parser.get_network_devices_settings_from_file(
            net_dev_output_file_path=net_dev_output_file
        )

        # Импортируем модуль с ожидаемой моделью
        try:
            module = importlib.import_module(expected_model_module)
        except ModuleNotFoundError:
            raise ImportError(f"Модуль {expected_model_module} не найден. Убедитесь, что он существует.")

        # Проверяем наличие result_model_dict
        if hasattr(module, 'result_model_dict'):
            expected_dict = module.result_model_dict
        else:
            raise AttributeError(f"Модуль {expected_model_module} не содержит 'result_model_dict'.")

        # Сравниваем устройства
        for key, expected_device in expected_dict.items():
            parsed_device = network_devices_dict.get(key)

            # Проверка наличия устройства
            self.assertIsNotNone(parsed_device, f"Устройство с индексом {key} отсутствует в результатах.")

            # Проверка полей устройства
            self.assertEqual(parsed_device.id, expected_device.id, f"Несовпадение id устройства {key}")
            self.assertEqual(parsed_device.name, expected_device.name, f"Несовпадение name устройства {key}")
            self.assertEqual(parsed_device.description, expected_device.description, f"Несовпадение description {key}")
            self.assertEqual(parsed_device.mac_address, expected_device.mac_address, f"Несовпадение mac_address {key}")
            self.assertEqual(parsed_device.status, expected_device.status, f"Несовпадение status {key}")

    return test_case


class TestNetworkDeviceParser(unittest.TestCase):
    pass


# Автоматически добавляем тесты для каждого подкаталога
test_cases_dir = 'tests/test_cases'
subdirectories = [
    os.path.join(test_cases_dir, d) for d in os.listdir(test_cases_dir) if os.path.isdir(os.path.join(test_cases_dir, d))
]

for subdir in subdirectories:
    test_case_name = f"test_{os.path.basename(subdir)}"
    test_func = create_test_case(subdir)
    setattr(TestNetworkDeviceParser, test_case_name, test_func)
