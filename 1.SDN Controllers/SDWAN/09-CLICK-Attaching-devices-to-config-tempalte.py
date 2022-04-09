# Let's take our application a step further in this step, no pun intended, and see how we can attach a configuration template
# that is available in vManage to devices in the SD-WAN fabric. Let's login into the DevNet Always on sandbox vManage GUI at
# this link with username devnetuser and password Cisco123!. On the left hand side in the expandable menu navigate to
# Configuration -> Templates and have a look at the VEDGE_BASIC_TEMPLATE and try to apply it to one of the vEdge devices.
# In this part of #the learning lab we will do the exact same steps but using the vManage REST API and Python code for the
# attach() function.

#The VEDGE_BASIC_TEMPLATE as you've seen has several parameters that can be changed and applied at the time of template
# attachment. These parameters are for the hostname, the IPv4 address on the loopback interface, the IPv4 address on the
# Gigabit0/0 interface, the system IP and the site ID. All these parameters will be passed into the attach function
# as @click.options. The template ID as well as the target device ID that the template will be attached to will also be
# passed in as options.

# Since we are making configuration changes with this function, the REST API call will be a POST and the endpoint that the
# call will be made to is https://{{vmanage}}:{{port}}/dataservice/template/device/config/attachfeature.
# If you are asking yourself how can you find the endpoint for attaching templates to devices, the answer is of course:
# the vManage REST API documentation.

#In the documentation we can also see that the payload is mandatory and should be similar to the one below:

{
  "deviceTemplateList":[
  {
    "templateId":"41f6a440-c5cc-4cc6-9ca1-af18e332a781",
    "device":[
    {
      "csv-status":"complete",
      "csv-deviceId":"5e5f45e7-3062-44b2-b6f6-40c682149e05",
      "csv-deviceIP":"172.16.255.11",
      "csv-host-name":"vm1",
      "//system/host-name":"vm1",
      "//system/system-ip":"172.16.255.11",
      "//system/site-id":"100",
      "csv-templateId":"41f6a440-c5cc-4cc6-9ca1-af18e332a781",
      "selected":"true"
    }
    ],
    "isEdited":false,
    "isMasterEdited":false
  }
  ]
}

# Based on the VEDGE_BASIC_TEMPLATE configuration template from the DevNet Sandbox vManage instance, we edit the payload
# with the parameter values we take as input from the user via the @click.option.
# Once the payload is built, the post_request method of the sdwanp instance is invoked and the response of this call is
# displayed to the user. The Python code for the attach function should look like the one below:

@click.command()
@click.option("--template", help="Name of the template to deploy")
@click.option("--target", help="Hostname of target network device.")
@click.option("--hostname", help="Hostname you wish the target has")
@click.option("--sysip", help="System IP you wish the target has")
@click.option("--loopip", help="Loopback interface IP address")
@click.option("--geip", help="Gigabit0/0 interface IP address")
@click.option("--siteid", help="Site ID")
#@click.argument("parameters", nargs=-1)
def attach(template, target, hostname, sysip, loopip, geip, siteid):
    """Attach a template with Cisco SDWAN.

        Provide all template parameters and their values as arguments.

        Example command:

          ./sdwan.py attach --template TemplateID --target TargetID --hostname devnet01.cisco.com
          --sysip 1.1.1.1 --loopip 2.2.2.2/24 --geip 3.3.3.3/24 --siteid 999
    """
    click.secho("Attempting to attach template.")

    payload = {
        "deviceTemplateList":[
        {
            "templateId":str(template),
            "device":[
            {
                "csv-status":"complete",
                "csv-deviceId":str(target),
                "csv-deviceIP":str(sysip),
                "csv-host-name":str(hostname),
                "/1/loopback1/interface/ip/address":str(loopip),
                "/0/ge0/0/interface/ip/address":str(geip),
                "//system/host-name":str(hostname),
                "//system/system-ip":str(sysip),
                "//system/site-id":str(siteid),
                "csv-templateId":str(template),
                "selected":"true"
            }
            ],
            "isEdited":"false",
            "isMasterEdited":"false"
        }
        ]
    }

    response = sdwanp.post_request('template/device/config/attachfeature', payload)
    print (response)

# Let's try out the function just defined and run the application with the attach option. In this case we will need to pass
# in all the required parameters and the way to do this is similar to:
# ./sdwan.py attach --template 72babaf2-68b6-4176-92d5-fa8de58e19d8 --target 100faff9-8b36-4312-bf97-743b26bd0211
# --hostname vedge03.cisco.com --sysip 4.4.4.62 --loopip 1.1.1.1/24 --geip 10.10.20.62/24 --siteid 555.
# In this case we are attaching the VEDGE_BASIC_TEMPLATE to vEdge03. The output should look similar to the one below:

# Attempting to attach template.
{"deviceTemplateList": [{"device": [{"csv-deviceId": "100faff9-8b36-4312-bf97-743b26bd0211", "//system/site-id": "555", "/0/ge0/0/interface/ip/address": "10.10.20.62/24", "csv-host-name": "vedge03.cisco.com", "csv-deviceIP": "4.4.4.62", "csv-status": "complete", "selected": "true", "//system/host-name": "vedge03.cisco.com", "csv-templateId": "72babaf2-68b6-4176-92d5-fa8de58e19d8", "/1/loopback1/interface/ip/address": "1.1.1.1/24", "//system/system-ip": "4.4.4.62"}], "isEdited": "false", "isMasterEdited": "false", "templateId": "72babaf2-68b6-4176-92d5-fa8de58e19d8"}]}
{u'id': u'push_feature_template_configuration-7e836030-17af-45a0-bfc6-c5a8cd81549c'}

# You can verify that the template was successfully applied by running the attached_devices option once more and passing
# in the template ID of VEDGE_BASIC_TEMPLATE.
