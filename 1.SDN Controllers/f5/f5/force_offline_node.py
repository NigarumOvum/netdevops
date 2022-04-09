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
 #print node.set_monitor_state(node_addresses=[ipaddress],states=['STATE_FORCED_DISABLED'])
 #print node.set_monitor_state(node_addresses=['10.4.161.149'],states=['STATE_ENABLED'])
 a=node.get_object_status(node_addresses=[ipaddress])
 print a[0].availability_status
 node.set_monitor_state(node_addresses=[ipaddress],states=['STATE_FORCED_DISABLED'])
 b= node.get_object_status(node_addresses=[ipaddress])
 print b[0].availability_status
 if b[0].availability_status == 'AVAILABILITY_STATUS_RED':
   print "%s Node Status: %s" %(ipaddress,b[0].availability_status)
 else :
  print "请检查是否正常关闭 %s" %(ipaddress)
 print node.get_monitor_status(node_addresses=[ipaddress])
