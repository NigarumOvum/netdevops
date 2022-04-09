import sys
sys.path.append("/pkg/bin")
from ztp_helper import ZtpHelpers
ztp_obj=ZtpHelpers()

#Provide a "reason" when configuring using xrapply()
reason_string="Testing out python xrapply() with the reason parameter"

response = ztp_obj.xrapply(filename=file_path, reason=reason_string)

from pprint import pprint
pprint(response)

#Check that the "reason" was committed to SYSDB
check_cmd = "show configuration commit list 1 detail"
response = ztp_obj.xrcmd({"exec_cmd" : check_cmd})

pprint(response)
