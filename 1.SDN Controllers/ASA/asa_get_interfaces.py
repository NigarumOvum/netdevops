#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')

    url = 'https://asa/api/monitoring/device/interfaces'
    response = requests.get(url, verify=False, auth=auth)

    print 'Status Code: ' + str(response.status_code)
    if response.text:
        parse = json.loads(response.text)
        print json.dumps(parse, indent=4)

