 from ncclient import manager
 import xmltodict
 import xml.dom.minidom

# Create an XML filter for targeted NETCONF queries
 netconf_filter = """
 <filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface></interface>
   </interface>
 </filter>"""

 with manager.connect(
         host=env_lab.IOS_XE_1["host"],
         port=env_lab.IOS_XE_1["netconf_port"],
         username=env_lab.IOS_XE_1["username"],
         password=env_lab.IOS_XE_1["password"],
         hostkey_verify=False
         ) as m:

With the active connection, next the <get-config> operation is executed, including the filter.

 netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

After the connection netconf_reply represents the rpc-reply from the device. In this line we print out the raw XML in a "pretty" fashion.

 print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

In these lines we convert the XML string that was returned to a Python Ordered Dictionary that can be easily manipulated, and then drill into the returned data to get a list of interfaces.

 # Parse the returned XML to an Ordered Dictionary
 netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

 # Create a list of interfaces
 interfaces = netconf_data["interfaces"]["interface"]

And finally, we loop over the interfaces, printing out the interface names and status.

 for interface in interfaces:
     print("Interface {} enabled status is {}".format(
             interface["name"],
             interface["enabled"]
             )
         )
