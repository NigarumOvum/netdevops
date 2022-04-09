#NodeAddress
# -*- coding: utf-8 -*-
import sys
import time
import csv
import ssl
reload(sys)
sys.path.append('./pycontrol')
import pycontrol.pycontrol as pc
#ssl._create_default_https_context = ssl._create_unverified_context
if len(sys.argv) != 5:
    print sys.argv[0] + ' ' + 'f5managedip' + ' ' + 'username' + ' ' + 'passwd' + ' ' + 'nodeip'
else :
 f5ip= sys.argv[1]
 username= sys.argv[2]
 passwd= sys.argv[3]
 nodeip= sys.argv[4]
 b = pc.BIGIP(
 hostname = f5ip,
 username = username,
 password = passwd,
 fromurl = True,
    wsdls=['LocalLB.NodeAddress'])
 node = b.LocalLB.NodeAddress
 ipaddress=nodeip
 a=node.get_object_status(node_addresses=[ipaddress])
 print a[0].availability_status
