from .controller import update_tracker_command

COMMAND_UPDATE_TRACKER = 'update-tracker'
COMMAND_SEARCH = 'search'


commands = [
    {
        'action': COMMAND_UPDATE_TRACKER,
        'help': 'update tracker server',
        'arguments': [
            {'dest':'--url', 'kwargs': dict(default=r'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt')}
        ]
    }
]