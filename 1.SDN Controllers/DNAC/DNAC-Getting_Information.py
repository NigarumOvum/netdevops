#STEP 1: Identify involved hosts
#Retieve host details from dnac-EM
source_host = host_list(dnac["host"], token, ip=destination_ip)

#Verify single host from IP
verify_single_host(source_host, source_ip)
verify_single_host(destination_host, destination_ip)

#Print out source details

Print(" Source Hosts Details:")
Print("-" * 25)
Print_hosts_details(source_host[0])

Print(" Destination Hosts Details:")
Print("-" * 25)
Print_hosts_details(destination_host[0])
