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
    print sys.argv[0] + ' ' + 'f5managedip' + ' ' + 'username' + ' ' + 'passwd' + ' ' + 'poolname'
else :
 poolname = sys.argv[4]
 a = pc.BIGIP(
  hostname = sys.argv[1],
  username = sys.argv[2],
  password = sys.argv[3],
  fromurl = True,
   wsdls=['LocalLB.PoolMember'])
 pool01 = a.LocalLB.PoolMember
 b= pool01.get_object_status(pool_names=[poolname])
 for x in b:
    for y in x:
        print poolname+'=>'+y.member.address+':'+str(y.member.port)+'=>'+y.object_status.availability_status+'=>'+y.object_status.enabled_status+'=>'+y.object_status.status_description
