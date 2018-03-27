from mvatv.plugin.plugin import Plugin
from mvatv.exception.exceptions import CantPlugingError
from mvatv.utils.utils import Quality
from mvatv.exception.exceptions import SearchInfoError, NoResourceError

import requests

class MVATV(object):

    plugins = list()

    @classmethod
    def plugging(cls, pluggable):
        if Plugin not in type(pluggable).__bases__:
            raise CantPlugingError('Your plugin must inherit Plugin class.')
        if not hasattr(pluggable, 'search'):
            raise CantPlugingError('Your plugin must implement search method.')
        if not hasattr(pluggable, 'get_type'):
            raise CantPlugingError('Your plugin must implement get_type method.')
            
        cls.plugins.append(pluggable)

    @classmethod
    def get_support_types(cls):
        print('enter get_s_t')
        return [plugin.get_type() for plugin in cls.plugins]

    @classmethod
    def search(cls, type, name, season, episode, quality, subscript):
        result = list()
        try:
            if season <= 0:
                raise SearchInfoError('season cannot be a nagetive number')
            if episode <= 0:
                raise SearchInfoError('episode cannot be a nagetive number')
            if quality not in ['High', 'Medium', 'Low']:
                raise SearchInfoError('quality must be High, Medium or Low')
            for plugin in [plugin for plugin in cls.plugins if plugin.get_type() == type]:
                result.append(plugin.search(name, season, episode, Quality[quality], subscript))
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
