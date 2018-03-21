from mvatv.plugin.plugin import Plugin
from mvatv.exception.exceptions import CantPlugingError


class MVATV(object):

    def __init__(self):
        self.plugins = list()

    def plugging(self, pluggable):
        if Plugin not in type(pluggable).__bases__:
            raise CantPlugingError('Your plugin must inherit Plugin class.')
        if not hasattr(pluggable, '_search'):
            raise CantPlugingError('Your plugin must implement _search method.')
        self.plugins.append(pluggable)