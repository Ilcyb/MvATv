from mvatv.utils.utils import update_tracker
from mvatv.aria2 import aria2_tracker_file_path
from mvatv.core.mvatv import MVATV
from mvatv.core.commands import COMMAND_SEARCH, COMMAND_UPDATE_TRACKER
from mvatv.exception.exceptions import SearchInfoError, NoResourceError

import requests

def update_tracker_command(action, tracker_file_path=aria2_tracker_file_path()):
    try:
        print('updating tracker ...')
        trackers = update_tracker(action.url)
        with open(tracker_file_path, 'w') as tracker_file:
            tracker_file.write('bt-tracker=' + trackers)
        print('complete')
    except Exception:
        print('update failed. Please check if the tracker server is available')

def search(action):
    try:
        result = MVATV.search(action.type, action.name, action.season, action.episode, action.quality, action.subscript)
        print(result)
        return result
    except SearchInfoError as e:
        print(e)
        return
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        print('Can\'t connect to the data source, please check the data source is normal')
        return
    except NoResourceError:
        print('No such resources')
        return
    except Exception as e:
        print('Unhandled exception occurred:', '\n', e)
        return


NAME2CONTROLLER_DICT = {
    COMMAND_UPDATE_TRACKER: update_tracker_command,
    COMMAND_SEARCH: search
}

def executor(action):
    func = NAME2CONTROLLER_DICT.get(action.command, None)
    if not callable(func):
        return
    else:
        func(action)