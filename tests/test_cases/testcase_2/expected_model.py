from src.models import SettingsModel

result_model_dict = {

    0:
        SettingsModel(
            id='LAN',
            name='ether2',
            description='LAN',
            mac_address='50:00:00:31:00:01',
            status='down'
        ),

    1:
        SettingsModel(
            id='ether1',
            name='ether1',
            description=None,
            mac_address='50:00:00:31:00:00',
            status='up'
        ),

    2:
        SettingsModel(
            id='ether3',
            name='ether3',
            description=None,
            mac_address='50:00:00:31:00:02',
            status='down'
        ),
}
