import requests
import json

def _execute_aria2c_rpc_command(method, host, params, id, **options):
    jsonreq = json.dumps({'jsonrpc':'2.0', 'id':id,
                            'method':method,
                            'params':[params, options]})
    aria2_return_info = requests.post(host, data=jsonreq)
    return aria2_return_info
