from dataclasses import dataclass


@dataclass
class SettingsModel:
    id: str
    name: str
    description: str
    mac_address: str
    status: str




