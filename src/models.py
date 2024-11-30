from dataclasses import dataclass


@dataclass
class SettingsModel:
    id: str
    name: str
    description: str | None
    mac_address: str
    status: str




