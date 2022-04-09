@click.group()
def cli():
    """Command line tool for deploying templates to CISCO SDWAN.
    """
    pass

@click.command()
def device_list():
    pass

@click.command()
def template_list():
    pass

@click.command()
def attached_devices():
    pass

@click.command()
def attach():
    pass

@click.command()
def detach():
    pass

cli.add_command(attach)
cli.add_command(detach)
cli.add_command(device_list)
cli.add_command(attached_devices)
cli.add_command(template_list)

if __name__ == "__main__":
    cli()
#We have 5 CLI commands that are grouped under the cli Group: device_list, template_list, attached_devices,
# attach and detach. The commands should be self explanatory and correspond to what we wanted the application
# to do from the beginning: get a list of all the devices in the SD-WAN fabric (device_list), a list of all the
# configuration templates on the vManage instance (template_list), a list of all the devices attached to a specific
# template (attached_devices), attach a configuration template to a device (attach) and detach a device from a configuration
# template (detach). In the snippet of code above all functions don't have at this point any code or functionality
# behind them. You can see that each one of them is just using pass. In the next sections of this learning lab we will
# start to populate each function with functional code to accomplish what we have planned.
