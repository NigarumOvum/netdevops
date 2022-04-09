# First we need to specify the endpoint, https://{{vmanage}}:{{port}} and then the login resource,/j_security_check.
# We will store each one of them in individual variables.
# The base_url_str variable contains the vManage endpoint in string format.
# The login_action variable contains the login resource.
# Next we need to specify the username and password and store it in another variable that we'll call login_data.
# This will be the payload data organized as key value pairs in JSON format that we send
# to the login resource. So far we have the three variables defined:

base_url_str = 'https://%s:8443/'%vmanage_ip

login_action = '/j_security_check'

login_data = {'j_username' : username, 'j_password' : password}

# We've decided to split the endpoint and resource into two different variables so
# that in case either of them change at any point in the future we can easily change them in only one place.
# Next we will combine these two variables to build the complete login URL.
# We name the variable login_url and define it as a combination of base_url_str and login_action.

# So far we have defined the login URL as a combination of endpoint and resource and the payload as a
# JSON file containing the j_username and j_password values. Next we will use the session method of the requests library
# to open a new session. We will use the post method of the session object to send the request to the login_url,
# with a payload of login_data and we don't want to check the authenticity of the self-signed certificate so
# the verify option is set to False.

login_url = base_url_str + login_action

sess = requests.session()

login_response = sess.post(url=login_url, data=login_data, verify=False)

# In order to make sure the login attempt was successful we verify the content returned and if there is a <html> tag in it
# we know the authentication failed, we return a message notifying the user that the Login Failed and we exit the function.
# We've seen in the Postman lab that for a successful authentication there is no data returned just a status of 200 OK.

if b'<html>' in login_response.content:
    print ("Login Failed")
    sys.exit(0)

# Bringing all these piece together we can finish building the first Python function to login and authenticate to a
# Cisco SD-WAN vManage REST API. This function will take as input 3 values: the vManage IP address, the username
# and password as you can see below:

def login(vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = 'https://%s:8443/'%vmanage_ip

        login_action = '/j_security_check'

        #Format data for loginForm
        login_data = {'j_username' : username, 'j_password' : password}

        #Url for posting login data
        login_url = base_url_str + login_action

        sess = requests.session()
        #If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)

        if b'<html>' in login_response.content:
            print ("Login Failed")
            sys.exit(0)

            
