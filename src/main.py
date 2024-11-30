import argparse

from NetworkDeviceParser import NetworkDeviceParser
from Serializer import Serializer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Парсер и сериализатор сетевых устройств.")
    parser.add_argument(
        '-i', '--input_file',
        required=True,
        help="Путь к входному файлу с данными сетевых устройств."
    )
    parser.add_argument(
        '-o', '--output_file',
        required=True,
        help="Путь к выходному файлу, куда будет записан результат в формате XML."
    )
    args = parser.parse_args()

    output_file_path: str = args.input_file
    result_xml_file_path: str = args.output_file

    device_parser = NetworkDeviceParser()
    serializer = Serializer()

    network_devices_dict = device_parser.get_network_devices_settings_from_file(
        net_dev_output_file_path=output_file_path
    )

    xml_string = serializer.serialize(
        dict_for_serialize=network_devices_dict
    )

    formatted_xml_strings = serializer.prettify_xml_string(
        xml_string=xml_string,
        with_recording_to_file=True,
        file_path=result_xml_file_path
    )
