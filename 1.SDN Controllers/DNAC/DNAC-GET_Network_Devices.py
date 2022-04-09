import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

token = get_auth_token() # Get a Token
    url = "https://sandboxdnac.cisco.com/api/v1/network-device" #Network Device endpoint
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'} #Build header Info
    resp = requests.get(url, headers=hdr)  # Make the Get Request
    device_list = resp.json() #capture the data from the controller
    print_device_list(device_list) #pretty print the data we want

 #Now let's apply a filter to the data and look for a specific device:
#Simply create a query string variable queryString and pass the variable part of the params parameter in your requests.get call. Code below

    token = get_auth_token() # Get a Token
    url = "https://sandboxdnac.cisco.com/api/v1/network-device" #Network Device endpoint
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'} #Build header Info
    querystring = {"macAddress":"00:c8:8b:80:bb:00","managementIpAddress":"10.10.22.74"}
    resp = requests.get(url, headers=hdr, params=querystring)  # Make the Get Request
    device_list = resp.json() # Capture data from the controller
    print_device_list(device_list) # Pretty print the data

if __name__ == "__main__":
    get_device_list()
