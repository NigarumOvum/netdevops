
# Print IOSXR configuration in lines

import sys
sys.path.append("/pkg/bin")
from ztp_helper import ZtpHelpers
ztp_obj=ZtpHelpers()

cmd={"exec_cmd" : "show running-config"}
ztp_obj.xrcmd(cmd)

#Order the output in the API
from pprint import pprint
pprint(ztp_obj.xrcmd(cmd))
