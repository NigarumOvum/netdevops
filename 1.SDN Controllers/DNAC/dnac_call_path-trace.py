url = "https://{}/api/v1/host".format(apic)
    headers["x-auth-token"] = ticket
    filters = []

#Next will get the network devices:

url = "https://{}/api/v1/network-device".format(apic)
    headers["x-auth-token"] = ticket

#Followed by gathering the interface details:

url = "https://{}/api/v1/interface/{}".format(apic, id)
headers["x-auth-token"] = ticket

#Here will run the flow-analysis API, which we discussed at the start of this section:

base_url = "https://{}/api/v1/flow-analysis".format(apic)
headers["x-auth-token"] = ticket

#In the last step of the Python scripts, we can use interface details to see if there are any problems within the path. At each hop in the network, this information provides the interface details, such as speed and VLAN information.

ingress = interface_details(apicem["host"], login,
                                    hop["ingressInterface"]["physicalInterface"]["id"])  # noqa: E501
        print_interface_details(ingress)
        print("Egress Interface")
        print("-" * 20)
        egress = interface_details(apicem["host"], login,
                                   hop["egressInterface"]["physicalInterface"]["id"])  # noqa: E501
        print_interface_details(egress)
