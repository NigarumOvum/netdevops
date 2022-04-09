import requests
from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

def get_device_int(device_id):
  """
  Building out function to retrieve device interface. Using requests.get to      make a call to the network device Endpoint
  """
  url = "https://sandboxdnac.cisco.com/api/v1/interface"
  hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
  querystring = {"macAddress": device_id} # Dynamically build the querey params to get device spefict Interface info
  resp = requests.get(url, headers=hdr, params=querystring)  # Make the Get  Request
  interface_info_json = resp.json()
  
  print_interface_info(interface_info_json)
