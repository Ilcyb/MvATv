import requests
from enum import Enum


class Quality(Enum):
    High = 1000
    Medium = 500
    Low = 200


def update_tracker(url):
    try:
        tracker_response = requests.get(url)
        tracker_response.raise_for_status()
        trackers = tracker_response.text.replace('\n\n', ',')
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError('Please check if the tracker source is available.')
    except Exception as e:
        raise
    else:
        return trackers
