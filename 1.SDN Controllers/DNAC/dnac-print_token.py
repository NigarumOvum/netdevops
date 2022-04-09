def apic_login(host, username, password):
    """
    Use the REST API to Log into an APIC-EM and retrieve ticket
    """
    url = "https://{}/api/system/v1/auth/token".format(host)

    # Make Login request and return the response body
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                headers=headers, verify=False)˜

    # print the token
    print(response.text)

apic_login(apicem['host'], apicem['username'], apicem['password'])
