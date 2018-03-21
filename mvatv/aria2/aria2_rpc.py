import requests
import json

def _execute_aria2c_rpc_command(method, host, params, id, **options):
    try:
        jsonreq = json.dumps({'jsonrpc':'2.0', 'id':id,
                                'method':method,
                                'params':[params, options]})
        aria2_return_info = requests.post(host, data=jsonreq)
        aria2_return_info.raise_for_status()
    except requests.exceptions.HTTPError:
        print('aria2c-rpc cannot process the request. Please check if the request is valid.')
    except requests.exceptions.ConnectionError:
        print('''The connection with aria2c-rpc was rejected.
        Please check if the host address and port number are correct.''')
    except Exception as e:
        print('Unhandled exception occurred:', '\n', e)
        return aria2_return_info

def addUri(host, uri, id, **options):
    response = _execute_aria2c_rpc_command('aria2.addUri', host, [uri], id, **options)
    response = json.loads(response.text)
    if response.get(id, 'None') == id:
        return response.get('result')
