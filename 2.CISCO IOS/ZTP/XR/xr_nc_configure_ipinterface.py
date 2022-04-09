#!/usr/bin/env python

from lxml import etree
from ncclient import manager

if __name__ == "__main__":

    with manager.connect(host='xrv', port=830, username='cisco', password='cisco',
                         hostkey_verify=False, device_params={'name': 'iosxr'},
                         allow_agent=False, look_for_keys=False) as device:


        nc_filter = """
            <config>
              <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
               <interface-configuration>
                <active>act</active>
                <interface-name>Loopback100</interface-name>
                <interface-virtual/>
                <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
                 <addresses>
                  <primary>
                   <address>100.100.1.1</address>
                   <netmask>255.255.255.0</netmask>
                  </primary>
                 </addresses>
                </ipv4-network>
               </interface-configuration>
              </interface-configurations>
            </config>
        """

        nc_reply = device.edit_config(target='candidate', config=nc_filter)
        print nc_reply
        device.commit()

