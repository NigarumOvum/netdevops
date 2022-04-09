from apicem import * # The apicem_config.py file is the place where you change the apic-em IP, username, password, and other attributes

def get_host_and_device():
    """
    This function returns a list of all hosts and network devices with a number tag.

    Return:
    -------
    list: A list of all hosts and network devices with a number tag
    """
    ip_list=[]
    idx=0
    # Get host
    try:
        resp= get(api="host")
        print ("Status of GET /host: ",resp.status_code)  # This is the http request status
        response_json = resp.json() # Get the json-encoded content from the response
        if response_json["response"] !=[]:
            i=0
            for item in response_json["response"]:
                i+=1
                ip_list.append([i,"host",item["hostIp"]])
            idx=i # idx(sequential number) is used to tag host and network device
    except:
        print ("Something went wrong. Cannot get the host IP list")
    # So far, "ip_list" contains all hosts

    # Now get the network device and append it to the list
    try:
        resp= get(api="network-device")
        print ("Status: of GET /network-device ",resp.status_code)  # This is the http request status
        response_json = resp.json() # Get the json-encoded content from response
        if response_json["response"] !=[]:
            for item in response_json["response"]:
                idx+=1
                ip_list.append([idx,"network device",item["managementIpAddress"]])
    except:
        print ("Something went wrong! Cannot get the network device IP list !")
    # Now "ip_list" should contain hosts and network devices

    if ip_list !=[]:
        return ip_list
    else:
        print ("There is no host or network device!")
        sys.exit()

######################################################################################################

if __name__ == "__main__": # Only run as a script
    # Use the tabulate module here to print a nice table format. You can use the pip tool to install it on your local computer
    # The tabulate module is imported in apicem.py
    # For simplicity, copy the source code into your working directory, without installing it
    print (tabulate(get_host_and_device(),headers=['number','type','ip'],tablefmt="rst"))
