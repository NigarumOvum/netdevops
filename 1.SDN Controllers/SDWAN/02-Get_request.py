# In this step we will create a new function that will use to GET data from the vManage REST API.
# Let's call the function to GET data - get_request(). For this function we plan to have as input two parameters,
# the vManage IP address and the resource from which we are trying to obtain the data from.
#  We'll call this resource a mount_point. Next we need to define the URL to which we will issue our GET request.
# From the vManage REST API documentation we've seen how the API is organized and where all the resources are found.
# All the REST API resources can be found after https://{{vmanage_ip}}:{{port}}/dataservice/.

# Having this in mind, we build the url as follows:

url = "https://%s:8443/dataservice/%s"%(vmanage_ip, mount_point)

# We can see the two variables that we take as input for the get_request() function, vmanage_ip and mount_point,
# get passed as string values in the process of building the URL.

# Next we use the requests library again but this time we don't build a new session, we merely use the request
# method to perform a GET on the url we've just built above and again we do not verify the authenticity of the SSL certificate.
# In a production environment you should definitely verify if the SSL certificate returned by the vManage instance is
# valid or not. We store the result of the request in a variable named response.
# We extract the content from the response and return it back to the user. The code for this part looks like the one below:

response = requests.request("GET", url, verify=False)
data = response.content
return data

# At this point we have all the components to build the GET function for Cisco SD-WAN vManage instances.
# Based on what we discussed so far and brining all the components together the get_request() function looks like below:

def get_request(vmanage_ip, mount_point):
    """GET request"""
    url = "https://%s:8443/dataservice/%s"%(vmanage_ip, mount_point)

    response = requests.request("GET", url, verify=False)
    data = response.content
    return data

# We will use this function whenever we want to perform a GET request from the vManage REST API.
# In the next step we will build a function to POST and create new data in the API.
