from mvatv.utils.utils import update_tracker
from mvatv.aria2 import aria2_tracker_file_path
from mvatv.core.commands import COMMAND_SEARCH, COMMAND_UPDATE_TRACKER

def update_tracker_command(action, tracker_file_path=aria2_tracker_file_path()):
    try:
        print('updating tracker ...')
        trackers = update_tracker(action.url)
        with open(tracker_file_path, 'w') as tracker_file:
            tracker_file.write('bt-tracker=' + trackers)
        print('complete')
    except Exception:
        print('update failed. Please check if the tracker server is available')

def search():
    pass

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