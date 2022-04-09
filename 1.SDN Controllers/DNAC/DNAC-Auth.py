import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

def get_auth_token():

#Building out Auth request. Using requests.post to make a call to the Auth Endpoint

    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'       # Endpoint URL
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token from the returned JSON
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token    # Create a return statement to send the token back for later use

# Finally, let's call the function we've created and retrieve our Token:

if __name__ == "__main__":
    get_auth_token()
