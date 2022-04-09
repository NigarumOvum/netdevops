from apicem import * # APIC-EM IP is assigned in apicem_config.py
import threading,time # This is needed for the delay - sleep() function

def check_status(arg,arg1):
    """
    Non-blocking wait function to check POST /flow-analysis status:
    INPROGRESS, COMPLETED, FAILED

    Parameters
    ----------
    arg (str) : status of POST /flow-analysis
    arg1 (str): flowAnalysisId from POST /flow-analysis
    Return:
    -------
    None
    """
    status = arg
    flowAnalysisId = arg1
    count = 0
    while status != "COMPLETED":
        if status == "FAILED":
            print("Unable to find the full path. No traceroute or netflow information was found. The path calculation failed.")
            print("\n------ End of path trace ! ------")
            sys.exit()
        print ("\nTask is not finished yet, sleep 1 second then try again")
        time.sleep(1)
        count += 1
        if count > 30: # timeout after ~ 30 seconds
            print ("\nScript timed out. No routing path was found. Please try using a different source and destination !")
            print("\n------ End of path trace ! ------")
            sys.exit()
        try:
            r = get(api="flow-analysis/"+flowAnalysisId)
            response_json = r.json()
            print ("Response from GET /flow-analysis/"+flowAnalysisId,json.dumps(response_json,indent=4))
            status = response_json["response"]["request"]["status"]
            print ("\n Check status here: ",status," \n")
        except:
            # Something is wrong
            print ("\nSomething went wrong while running get /flow-analysis/{flowAnalysisId}")
    print("\n------ End of path trace ! ------")

def get_host_and_device():
    """
    This function returns a list of all hosts and network devices with a number tag.

    Return:
    ------
    list: A list of all hosts and network devices with a number tag
    """
    ip_list=[]
    idx=0
    # Create a list of host and network device
    # Get host
    try:
        resp= get(api="host")
        response_json = resp.json() # Get the json-encoded content from the response
        i=0
        if response_json["response"] !=[]:
            for item in response_json["response"]:
                i+=1
                ip_list.append([i,"host",item["hostIp"]])
            idx=i # This idx(sequential number) is used to tag host and network device
                  # So far this number = the number of hosts
    except:
        print ("Something went wrong. Cannot get the host IP list")

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
        print ("Something went wrong! Cannot get the network device IP list!")
    # Now "ip_list" should have hosts and network devices
    return ip_list

def select_ip(prompt,ip_list,idx):
    """
    This function returns an element that the user-selected from a tabular list

    Parameters
    ----------
    prompt: str
        A message used to prompt the user
    ip_list: list
        A list with idx that enables a user to make a selection
    idx: int
        The position of the element to retrieve from the list

    Return:
    -------
    str: The user selected IP address
    """

    ip =""
    while True:
        user_input = input(prompt)
        user_input= user_input.lstrip() # Ignore leading space
        if user_input.lower() == 'exit':
            sys.exit()
        if user_input.isdigit():
            if int(user_input) in range(1,len(ip_list)+1):
                ip = ip_list[int(user_input)-1][idx] # The idx is the position of IP
                return ip
            else:
                print ("Oops! The number you selected is out of range. Please try again or enter 'exit'")
        else:
            print ("Oops! The input you entered is not a number. Please try again or enter 'exit'")
    # End of while loop

##########################################################################

if __name__ == "__main__": # Only run as a script
    ip_idx = 2
    nd_list = get_host_and_device()
    if len(nd_list) < 2:
        print ("You need at least two hosts or network devices to perform a path trace!")
        sys.exit()

    print (tabulate(nd_list,headers=['number','type','ip'],tablefmt="rst"))
    print (" Note: Not all source/destination ip address pairs will return a path. No route!  \n")
    s_ip = select_ip('=> Select a number for the source IP from the list shown: ',nd_list,ip_idx) # ip_idx (=2) is the position of IP in the list
    d_ip = select_ip('=> Select a number for the destination IP from the list shown: ',nd_list,ip_idx) # ip_idx (=2) is the position of IP in the list
    # Now that you have the source and destination IP addresses you can use them to POST /flow-analysis
    path_data = {"sourceIP": s_ip, "destIP": d_ip} # JSON input for POST /flow-analysis
    r = post(api="flow-analysis",data=path_data) # Run POST /flow-analysis
    response_json = r.json()
    print ("Response from POST /flow-analysis:\n",json.dumps(response_json,indent=4))
    try:
       flowAnalysisId = response_json["response"]["flowAnalysisId"]
    except:
        print ("\n For some reason, you cannot get the flowAnalysisId")
        sys.exit()

    ###########################################################
    # Check status of POST /flow-analysis - non-blocking wait #
    ###########################################################
    thread = threading.Thread(target=check_status, args=('',flowAnalysisId,)) # Passing
    thread.start()
