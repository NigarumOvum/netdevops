 from ncclient import manager
 import xmltodict
 import xml.dom.minidom

  # Create an XML configuration template for ietf-interfaces
 netconf_interface_template = """
 <config>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface>
             <name>{name}</name>
             <description>{desc}</description>
             <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                 {type}
             </type>
             <enabled>{status}</enabled>
             <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                 <address>
                     <ip>{ip_address}</ip>
                     <netmask>{mask}</netmask>
                 </address>
             </ipv4>
         </interface>
     </interfaces>
 </config>"""

Next the script asks the user for the details on a new Loopback interface to add.

 # Ask for the Interface Details to Add
 new_loopback = {}
 new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
 new_loopback["desc"] = input("What description to use? ")
 new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
 new_loopback["status"] = "true"
 new_loopback["ip_address"] = input("What IP address? ")
 new_loopback["mask"] = input("What network mask? ")

Here the template is combined with the data from the user.

 # Create the NETCONF data payload for this interface
 netconf_data = netconf_interface_template.format(
         name = new_loopback["name"],
         desc = new_loopback["desc"],
         type = new_loopback["type"],
         status = new_loopback["status"],
         ip_address = new_loopback["ip_address"],
         mask = new_loopback["mask"]
     )

Lastly, here the <edit-config> operation is executed.

 netconf_reply = m.edit_config(netconf_data, target = 'running')

  netconf_interface_template = """
 <config>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface operation="delete">
             <name>{name}</name>
         </interface>
     </interfaces>
 </config>"""
