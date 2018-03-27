from mvatv.core.mvatv import MVATV
from mvatv.utils.utils import Quality
from mvatv.plugin.data_sources import ZIMUZU

COMMAND_UPDATE_TRACKER = 'update-tracker'
COMMAND_SEARCH = 'search'


commands = [
    {
        'action': COMMAND_UPDATE_TRACKER,
        'help': 'update tracker server',
        'arguments': [
            {'dest':'--url', 'kwargs': dict(default=r'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt')}
        ]
    },
    {
        'action': COMMAND_SEARCH,
        'help': 'search available resource',
        'arguments':[
            {'dest':'--type', 'kwargs': dict(choices=['tv'])}, # FIXME: 修复无法自动从MVATV.get_support_types获取类型的错误
            {'dest':'--name', 'kwargs': dict(required=True)},
            {'dest':'--season', 'kwargs': dict(default=1,type=int)},
            {'dest':'--episode', 'kwargs': dict(default=1,type=int)},
            {'dest':'--quality', 'kwargs': dict(default='Medium',help='resource quality; High, Medium or Low')},
            {'dest':'--subscript', 'kwargs': dict(action='store_true', help='whether need subscript')}
        ]
    }
]