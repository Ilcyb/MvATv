import base64
import requests
import json

def _execute_aria2c_rpc_command(method, host, params, id, *status, **options):
    try:
        all_params = list(status)
        if params != None:
            all_params.insert(0, params)
        if len(options) != 0:
            all_params.append(options)
        jsonreq = json.dumps({'jsonrpc':'2.0', 'id':id,
                        'method':method,
                        'params':all_params})
        aria2_return_info = requests.post(host, data=jsonreq)
        aria2_return_info.raise_for_status()
    except requests.exceptions.HTTPError:
        print('aria2c-rpc cannot process the request. Please check if the request is valid.')
    except requests.exceptions.ConnectionError:
        print('''The connection with aria2c-rpc was rejected.
        Please check if the host address and port number are correct.''')
    except Exception as e:
        print('Unhandled exception occurred:', '\n', e)
    else:
        return aria2_return_info

def addUri(host, uri, id, **options):
    response = _execute_aria2c_rpc_command('aria2.addUri', host, [uri], id, **options)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def addTorrent(host, torrent_file_path, id, **options):
    with open(torrent_file_path, 'rb') as target:
        torrent = base64.b64encode(target.read())
    response = _execute_aria2c_rpc_command('aria2.addTorrent', host, torrent, id, **options)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def addMetalink(host, meta_file_path, id, **options):
    with open(meta_file_path, 'rb') as target:
        meta = base64.b64encode(target.read())
    response = _execute_aria2c_rpc_command('aria2.addMetalink', host, meta, id, **options)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def remove(host, gid, id):
    response = _execute_aria2c_rpc_command('aria2.remove', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def forceRemove(host, gid, id):
    response = _execute_aria2c_rpc_command('aria2.forceRemove', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def pause(host, gid, id):        
    response = _execute_aria2c_rpc_command('aria2.pause', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def pauseAll(host, id):
    response = _execute_aria2c_rpc_command('aria2.pauseAll', host, None, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def forcePause(host, gid, id):
    response = _execute_aria2c_rpc_command('aria2.forcePause', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def forcePauseAll(host, id):
    response = _execute_aria2c_rpc_command('aria2.forcePauseAll', host, None, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def unpause(host, gid, id):
    response = _execute_aria2c_rpc_command('aria2.unpause', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def unpauseAll(host, id):
    response = _execute_aria2c_rpc_command('aria2.unpauseAll', host, None, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return True, response.get('result')
        else:
            return False, response.get('error')

def tellStatus(host, gid, id, *status):
    response = _execute_aria2c_rpc_command('aria2.tellStatus', host, gid, id, *status)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def getUris(host, gid, id):
    response = _execute_aria2c_rpc_command('aria2.getUris', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def getFiles(host, gid, id):
    response = _execute_aria2c_rpc_command('aria2.getFiles', host, gid, id)
    response = json.loads(response.text)
    if response.get('id', 'None') == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def tellActive(host, id, *status):
    response = _execute_aria2c_rpc_command('aria2.tellActive', host, None, id, *status)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def tellWaiting(host, id, offset=0, num=10, *status):    
    status = (offset, num, *status)
    response = _execute_aria2c_rpc_command('aria2.tellWaiting', host, None, id, *status)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def tellStopped(host, id, offset=0, num=10, *status):
    status = (offset, num, *status)    
    response = _execute_aria2c_rpc_command('aria2.tellStopped', host, None, id, *status)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def changePosition(host, gid, id, pos, how='POS_SET'):
    status = (pos, how)
    response = _execute_aria2c_rpc_command('aria2.changePosition', host, gid, id, *status)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def changeOption(host, gid, id, **options):
    response = _execute_aria2c_rpc_command('aria2.changeOption', host, gid, id, **options)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

def getGlobalStat(host, id):
    response = _execute_aria2c_rpc_command('aria2.getGlobalStat', host, None, id)
    response = json.loads(response.text)
    if response.get('id', None) == id:
        if 'error' not in response:
            return False, response.get('error')
        else:
            return True, response.get('result')

