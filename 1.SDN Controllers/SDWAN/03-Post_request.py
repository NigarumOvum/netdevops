# We've built so far two functions for the vManage REST API: login(vmanage_ip, username, password)
# and get_request(vmanage_ip, mount_point). Next let's build the function to perform POST calls and create new data in the API.
# We will call this function post_request(). Similarly to the get_request() function, the post_request() function
# takes as input two parameters: one is the vManage instance IP address and the second one is the resource to which the
# POST call will be sent to. Unlike the get_request() function, the POST function takes two more parameters as input:
# the payload that will be sent to the endpoint and the Content-Type header will be enforced as application/json.

# First we build the URL to which the request will be sent to. This variable is exactly the same as the one we used
# for the GET function. Just like in the case of get_request(), the resources that we can send the POST request to,
# are all to be found after https://{{vmanage_ip}}:{{port}}/dataservice/.
# The payload data that will be sent with the request is taken from the input of the function, is JSON encoded and stored
# in the payload variable. So far the POST function should look like below:

def post_request(vmanage_ip, mount_point, payload, headers={'Content-Type': 'application/json'}):
    url = "https://%s:8443/dataservice/%s"%(vmanage_ip, mount_point)
    payload = json.dumps(payload)

# Next we perform the actual POST operation. We use again the request method from the requests library,
# we specify that this is a POST operation, the endpoint and resource represented by the URL we defined above,
# the actual data that will be sent with this call stored in the payload variable, the Content-Type headers and the
# SSL verification is disabled. The result of the request is stored in the response variable. The json() method is
# called on the response object and the JSON format of the response is returned to the user.
# The Python code should look like the one below:

response = requests.request("POST", url, data=payload, headers=headers, verify=False)
data = response.json()
return data

#If we bring all these pieces together the post_request() function looks like below:

def post_request(vmanage_ip, mount_point, payload, headers={'Content-Type': 'application/json'}):
    """POST request"""
    url = "https://%s:8443/dataservice/%s"%(vmanage_ip, mount_point)
    payload = json.dumps(payload)

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    data = response.json()
    return data
