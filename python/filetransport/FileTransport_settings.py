##############################################################################
# Incoming 

RULES = [
    {
        'source': 'endpoint1',
        'match': '*/incoming/*.tsv',
        'dest': ['endpoint2','endpoint3']
    },
    {
        'source': 'endpoint2',
        'match': '*/outgoing/*.tsv',
        'dest': ['endpoint1']
    }
]



##############################################################################
# Endpoints

ENDPOINTS = [
    {
        'name': 'endpoint1',
        'type': 'sftp',
        'path': 'sftp://hostname:port/databank/account_id1',
        'timeout': 120
    },
    {
        'name': 'endpoint2',
        'type': 'fs',
        'path': 'fs:///databank_loal/account_id1'
        'timeout': 10
    },
    {
        'name': 'endpoint3',
        'type': 'smtp',
        'path': 'databank_admin@gmail.com',
        'timeout': 10
    }
]