#Create the local configuration file
file_path="/root/gig0up.conf"

file_content="""

!
interface GigabitEthernet0/0/0/0
  ipv4 address 100.1.1.10/24
  no shutdown
!
end

with open(file_path, 'w') as fd:
     fd.write(file_content)

#Import ZtpHelpers from /pkg/bin/ztp_helper.py
sys.path.append("/pkg/bin")
from ztp_helper import ZtpHelpers
ztp_obj=ZtpHelpers()

#Do a configuration merge using xrapply
response=ztp_obj.xrapply(filename=file_path

#Check the return value
from pprint import pprint
pprint(response)

#Let's verify that the interface is up as expected:
response=ztp_obj.xrcmd({"exec_cmd" : "show ipv4 interface brief"})
pprint(response)
