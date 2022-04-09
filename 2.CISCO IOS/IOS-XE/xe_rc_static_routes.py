#!/usr/bin/env python

import requests
import json
import time
import collections
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vndyang.data+json'
    }

    print 'API Call #1 - DISPLAY CURRENT ROUTES with NEXT-HOPS'
    print '-----------'

    url = 'http://csr1kv/restconf/api/config/native/ip/route?deep'
    response = requests.get(url, verify=False, headers=headers, auth=auth)

    print 'Status Code: ' + str(response.status_code)
    if response.text:
        parse = json.loads(response.text)
        print json.dumps(parse, indent=4)

    time.sleep(2)

    print 'API Call #2 - ADD ROUTES'
    print '-----------'

    url = 'http://csr1kv/restconf/api/config/native/route'

    route = collections.OrderedDict()

    route['prefix'] = '50.40.40.0'
    route['mask'] = '255.255.255.0'
    route['fwd-list'] = [{'fwd': '192.168.1.1'}]
    ip_route_list = [route]

    routes_to_add = {
        "ned:route": {
            "ip-route-interface-forwarding-list": ip_route_list
        }
    }

    response = requests.post(url, data=routes_to_add, verify=False, headers=headers, auth=auth)

    print 'Status Code: ' + str(response.status_code)
    if response.text:
        parse = json.loads(response.text)
        print json.dumps(parse, indent=4)

    time.sleep(2)

    print 'API Call #3 - VERIFY ROUTES ADDED'
    print '-----------'

    url = 'http://csr1kv/restconf/api/config/native/ip/route?deep'
    response = requests.get(url, verify=False, headers=headers, auth=auth)

    print 'Status Code: ' + str(response.status_code)
    if response.text:
        parse = json.loads(response.text)
        print json.dumps(parse, indent=4)


