#So far we've built three functions that we will re-use extensively in our interactions with the vManage REST API: login(),
# get_request() and post_request(). In this step we will create our first Python class. Classes in Python provide a means
# of bundling data and functionality together. Creating a new class creates a new type of object that can then be instantiated.
# Each class instance can have attributes attached to it for state maintenance and also methods for modifying its state.
# The __init__ method is a reserved method in Python classes and is called a constructor.
# With it we can initialize the attributes of the class. self represents the instance of a class and with it we can
# access the attributes and the methods of the class.

# We will initialize the constructor __init__ method with the attributes for the vManage IP address,
# an empty dictionary for the REST API session and we will also initialize the login function.
# After that we start to define the methods that the rest_api_lib class will expose when an instance of it is created.
# Here we reuse as much as possible the functions we defined so far in this Learning Lab for login, get_request()
# and post_request. There are only small adjustments that need to be done on the functions we developed so far to
# adapt them for being methods in the Python class. First difference is that each method in a Python class needs
# to have the self parameter passed as input. The other difference is that we preserve the session that gets
# established after we login into the API and use this session in the other methods of the class.

# Having in mind all of this additional information and the functions we defined in the previous steps,
# the rest_api_lib class should look similar to the one below:

class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)

    def login(self, vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = 'https://%s:8443/'%vmanage_ip

        login_action = '/j_security_check'

        #Format data for loginForm
        login_data = {'j_username' : username, 'j_password' : password}

        #Url for posting login data
        login_url = base_url_str + login_action
        url = base_url_str + login_url

        sess = requests.session()
        #If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)


        if b'<html>' in login_response.content:
            print ("Login Failed")
            sys.exit(0)

        self.session[vmanage_ip] = sess

    def get_request(self, mount_point):
        """GET request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
        #print url
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = response.content
        return data

    def post_request(self, mount_point, payload, headers={'Content-Type': 'application/json'}):
        """POST request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
        payload = json.dumps(payload)
        print (payload)

        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        data = response.json()
        return data
