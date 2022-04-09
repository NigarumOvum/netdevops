# In this step, let's take the CLI application further and get a list of all devices attached to a configuration template.
# Unlike the device_list and template_list functions that did not take any parameters, the attached_devices function needs
# as input the template ID in order to return the list of devices attached to it. In order to pass in parameters to the
# function, the click library provides @click.option(). You can specify as many options as you want and also provide a
#  description for what each option means.

# Next we need to build the URL that specifies the resource in the vManage REST API that will return the devices attached
# to the template. By reading the vManage REST API documentation and looking at the swagger documentation,
# the resource that we need to do the GET call to is in this case:
# https://{{vmanage}}:{{port}}/dataservice/template/device/config/attached/templateId.
# Using the session to vManage that is already opened in the sdwanp instance of the rest_api_lib class,
# we get_request on this resource and store the returned data in a variable called response.

# Similarly to what we've done with the previous functions, from the data that is returned by the API we extract only
# information pertaining to the hostname, device IP, site ID, host ID and host type and use tabulate to display the data
# to the user. The code for the attached_devices function should look similar to the one below:

@click.command()
@click.option("--template", help="Name of the template you wish to retrieve information for")
def attached_devices(template):
    """Retrieve and return devices associated to a template.

        Example command:

            ./sdwan.py attached_devices --template abcd1234567890

    """

    url = "template/device/config/attached/{0}".format(template)

    response = json.loads(sdwanp.get_request(url))
    items = response['data']

    headers = ["Host Name", "Device IP", "Site ID", "Host ID", "Host Type"]
    table = list()

    for item in items:
        tr = [item['host-name'], item['deviceIP'], item['site-id'], item['uuid'], item['personality']]
        table.append(tr)
    try:
        click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))

# Let's run the application and see the output of the new function.
 # If we pass in the attached_devices parameter together with the template ID that we've obtained in the previous step
 # like so ./sdwan.py attached_devices --template 72babaf2-68b6-4176-92d5-fa8de58e19d8 the output should look similar
 # to the one below if there is at least a device attached to the template:
