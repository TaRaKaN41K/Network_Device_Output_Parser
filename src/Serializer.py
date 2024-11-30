import xml.etree.ElementTree as ET
from xml.dom import minidom
from dataclasses import asdict


class Serializer:

    @staticmethod
    def dataclass_to_xml(obj):
        root = ET.Element("Device")

        for field, value in asdict(obj).items():
            field_element = ET.SubElement(root, field)
            field_element.text = str(value)

        return root

    @staticmethod
    def prettify_xml_string(xml_string: str, with_recording_to_file: bool, file_path: str = "network_devices.xml") -> str:
        xml_string = f"<NetworkDevices>{xml_string}</NetworkDevices>"
        parsed_xml = minidom.parseString(xml_string)
        pretty_xml = parsed_xml.toprettyxml(indent="\t")

        if with_recording_to_file:
            with open(file_path, "w") as file:
                file.write(pretty_xml)

            return pretty_xml

        return pretty_xml

    def serialize(self, dict_for_serialize: dict) -> str:

        xml_string: str = ''

        for i in range(len(dict_for_serialize)):
            root = self.dataclass_to_xml(dict_for_serialize[i])
            xml_str = ET.tostring(root, encoding='unicode', method='xml')
            xml_string += xml_str

        return xml_string
