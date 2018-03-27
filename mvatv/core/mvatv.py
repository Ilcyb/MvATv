from mvatv.plugin.plugin import Plugin
from mvatv.exception.exceptions import CantPlugingError
from mvatv.utils.utils import Quality
from mvatv.exception.exceptions import SearchInfoError, NoResourceError

import requests

class MVATV(object):

    def __init__(self):
        self.plugins = list()

    def plugging(self, pluggable):
        if Plugin not in type(pluggable).__bases__:
            raise CantPlugingError('Your plugin must inherit Plugin class.')
        if not hasattr(pluggable, 'search'):
            raise CantPlugingError('Your plugin must implement search method.')
        if not hasattr(pluggable, 'get_type'):
            raise CantPlugingError('Your plugin must implement get_type method.')
            
        self.plugins.append(pluggable)

    def get_support_types(self):
        return [plugin.get_type() for plugin in self.plugins]

    def search(self, type, name, season, episode, quality, subscript):
        result = list()
        try:
            if season <= 0:
                raise SearchInfoError('season cannot be a nagetive number')
            if episode <= 0:
                raise SearchInfoError('episode cannot be a nagetive number')
            if quality not in ['High', 'Meduim', 'Low']:
                raise SearchInfoError('quality must be High, Meduim or Low')
            for plugin in [plugin for plugin in self.plugins if plugin.get_type() == type]:
                result.append(plugin.search(name, season, episode, Quality['quality'], subscript))
            result = [r for r in result if result != None]
            if len(result) == 0:
                raise NoResourceError
        except SearchInfoError:
            raise
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
            raise
        except Exception:
            raise
        else:
            return result
