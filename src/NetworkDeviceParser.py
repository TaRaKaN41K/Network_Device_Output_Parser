import re

from src.models import SettingsModel
from src.regex import ID_REGEX, NAME_REGEX, DESCRIPTION_REGEX, MAC_ADDRESS_REGEX, STATUS_REGEX


class NetworkDeviceParser:

    def __init__(self):
        self.network_devices: dict[int, SettingsModel] = {}

    @staticmethod
    def __get_id(settings_text: str) -> str | None:

        pattern = ID_REGEX

        match = re.search(pattern, settings_text)
        if match:
            return str(match.group(1))
        else:
            return None

    @staticmethod
    def __get_name(settings_text: str) -> str | None:

        pattern = NAME_REGEX

        match = re.search(pattern, settings_text)
        if match:
            return str(match.group(1))
        else:
            return None

    @staticmethod
    def __get_description(settings_text: str) -> str | None:

        pattern = DESCRIPTION_REGEX

        match = re.search(pattern, settings_text)
        if match:
            return str(match.group(1))
        else:
            return None

    @staticmethod
    def __get_mac_address(settings_text: str) -> str | None:

        pattern = MAC_ADDRESS_REGEX

        match = re.search(pattern, settings_text)
        if match:
            return str(match.group(1))
        else:
            return None

    @staticmethod
    def __get_status(settings_text: str) -> str | None:

        pattern = STATUS_REGEX

        match = re.search(pattern, settings_text, re.MULTILINE)
        if match and str(match.group(1)) == "R":
            return "up"
        else:
            return "down"

    def get_network_devices_settings_from_file(self, net_dev_output_file_path: str) -> dict[int, SettingsModel]:

        self.network_devices = {}

        with open(net_dev_output_file_path, 'r', encoding='utf-8') as file:
            text = file.read().split('\n \n')

        for counter, section in enumerate(text):

            dev_id = self.__get_id(settings_text=section)
            name = self.__get_name(settings_text=section)
            desc = self.__get_description(settings_text=section)
            mac_address = self.__get_mac_address(settings_text=section)
            status = self.__get_status(settings_text=section)

            if dev_id or desc or name or mac_address or status:

                self.network_devices[counter] = SettingsModel(
                    id=dev_id,
                    name=name,
                    description=desc,
                    mac_address=mac_address,
                    status=status
                )

        return self.network_devices

