#LIST DEVICS
#In this step let's start to populate the device_list and template_list functions with working code. If you remember from previous learning labs in this module, the REST API endpoint and resource that we accessed to get information about all the devices in the fabric was https://{{vmanage}}:{{port}}/dataservice/device. We already have a session established with the vManage server in the instance of the rest_api_lib class that we called sdwanp. We will use the get_request method of this object to get a list of all the devices in the fabric and store the JSON data that is returned by the API in the response variable.

Next we extract just the [data] portion of the JSON and store it in a variable called items. The items variable at this point contains all the devices in the fabric and a lot of additional data about each of them as we've seen in previous learning labs. You can see the contents of the items variable when we use the https://sandboxsdwan.cisco.com:8443 vManage instance below:

@click.command()
def device_list():
    """Retrieve and return network devices list.

        Returns information about each device that is part of the fabric.

        Example command:

            ./sdwan.py device_list

    """
    click.secho("Retrieving the devices.")

    response = json.loads(sdwanp.get_request('device'))
    items = response['data']

    headers = ["Host-Name", "Device Type", "Device ID", "System IP", "Site ID", "Version", "Device Model"]
    table = list()

    for item in items:
        tr = [item['host-name'], item['device-type'], item['uuid'], item['system-ip'], item['site-id'], item['version'], item['device-model']]
        table.append(tr)
    try:
        click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))

        #The template_list() function is very similar to the device_list() one. The main difference is the REST API endpoint that we are accessing. In this case is the https://{{vmanage}}:{{port}}/dataservice/template/device and the data we extract from the returned JSON is about the Template Name, Device Type, Template ID, Attached devices and Template version. We use tabulate again to display the data to the user. The code for template_list() is below:


        @click.command()
def template_list():
    """Retrieve and return templates list.

        Returns the templates available on the vManage instance.

        Example command:

            ./sdwan.py template_list

    """
    click.secho("Retrieving the templates available.")

    response = json.loads(sdwanp.get_request('template/device'))
    items = response['data']

    headers = ["Template Name", "Device Type", "Template ID", "Attached devices", "Template version"]
    table = list()

    for item in items:
        tr = [item['templateName'], item['deviceType'], item['templateId'], item['devicesAttached'], item['templateAttached']]
        table.append(tr)
    try:
        click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))
