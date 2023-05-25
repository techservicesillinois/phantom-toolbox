#!/usr/bin/env python
# DO NOT EDIT - Update techservicesillinois/splunk-soar-template first

import base64
import json
import requests

def deploy(args):
    file_contents = open(args.file, 'rb').read()
    encoded_contents = base64.b64encode(file_contents)
    payload = {'app': encoded_contents.decode('ascii')}
    headers = {'ph-auth-token': args.token}
    result = requests.post(f'https://{args.hostname}/rest/app',
                           headers=headers,
                           data=json.dumps(payload))
    print(result.text)

    if result.status_code != requests.codes.ok or 'failed' in result.json():
        return 1
    return 0
