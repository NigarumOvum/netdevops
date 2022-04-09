To craft a custom RPC, we'll be leveraging another object from the ncclient package. Here we import xml_.

 from ncclient import manager, xml_

Rather than creating a NETCONF <filter> or <config>, this time we are explicitly calling the RPC from a model.
  save_body = """
 <cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
 """
 As we are sending a custom RPC, we use the dispatch method to send the custom operation.

 netconf_reply = m.dispatch(xml_.to_ele(save_body))
