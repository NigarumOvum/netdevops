#NodeAddress
import sys
import pycontrol.pycontrol as pc
import time
import csv
import ssl
if len(sys.argv) != 6:
    print sys.argv[0] + ' ' + 'f5managedip' + ' ' + 'username' + ' ' + 'passwd' + ' ' + 'poolname' +'ip:port'
else :
 hostname = sys.argv[1]
 username = sys.argv[2]
 password = sys.argv[3]
 poolname = sys.argv[4]
 member=sys.argv[5]
 members=[member]
 pool=poolname
 #ssl._create_default_https_context = ssl._create_unverified_context
 b = pc.BIGIP(hostname=hostname, username=username, password=password,fromurl = True,wsdls=['LocalLB.PoolMember','LocalLB.Pool'])

 def member_factory(b, member):
  ip,port = member.split(':')
  pmem = b.LocalLB.PoolMember.typefactory.create('Common.IPPortDefinition')
  pmem.address = ip
  pmem.port = int(port)
  return pmem

 def session_state_factory(b, members):
    session_states=[]
    for x in members:
        print x
        sstate = b.LocalLB.PoolMember.typefactory.create('LocalLB.PoolMember.MemberSessionState')
        sstate.member = member_factory(b, x)
        #sstate.session_state = 'STATE_FORCED_DISABLED'
        sstate.session_state = 'STATE_DISABLED'
        #SESSION_STATUS_ADDRESS_DISABLED
        #sstate.session_state = 'AVAILABILITY_STATUS_GRAY'
        session_states.append(sstate)
        #print session_states
    return session_states
 # The session state sequence object. Takes a list of 'member session state'
 # objects.Wrap the members in a LocalLB.PoolMember.MemberSessionStateSequence
 sstate_seq = b.LocalLB.PoolMember.typefactory.create('LocalLB.PoolMember.MemberSessionStateSequence')

 # 'item' is an attribute that maps to a list of 'Common.IPPortDefinition' objects.
 sstate_seq.item = session_state_factory(b, members)
 b.LocalLB.PoolMember.set_session_enabled_state(pool_names=[poolname],session_states=[sstate_seq])


