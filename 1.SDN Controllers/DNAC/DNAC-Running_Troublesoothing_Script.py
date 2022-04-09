#Entry point of the program

if __name__ == "__main__":

#Setup arg parse for command line parameters

import argparse
parser = argparse.ArgumentParser()

#Command line parameters for source and destination IP
parser.add_arguument("source_ip", help - "Source IP Add")
parser.add_arguument("destination_ip", help = "Destinastion Ip add")
args = parser.parse_args()

#Get source and destination Ips from command line
source_ip = args.source_ip
destination_ip = args.destination_ip

#Print Starting Message
Print(" Running Troublesoothing Script for")
Print("  Sorce IP::{}".format("source_ip")
Print("  Destination IP:{}".format(destiantion_ip))
Print("")
#Log in the dnac-EM Controller to get ticket
token = dnac_login(dnac["host"],
dnac["port"],
dnac["username"],
dnac["password"])
