from NetworkDeviceParser import NetworkDeviceParser
from Serializer import Serializer


if __name__ == '__main__':
    parser = NetworkDeviceParser()
    serializer = Serializer()

    network_devices_dict = parser.get_network_devices_settings_from_file(
        net_dev_output_file_path='./network_device_output.txt'
    )

    xml_string = serializer.serialize(
        dict_for_serialize=network_devices_dict
    )

    formatted_xml_strings = serializer.prettify_xml_string(
        xml_string=xml_string,
        with_recording_to_file=True
    )
