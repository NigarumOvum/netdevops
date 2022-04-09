
Python Script

Python scripts can run in non-interactive mode by providing the Python script name as an argument in the Python command. Python scripts must be accessible from within the Guest Shell. To access Python scripts from the Guest Shell, save the scripts in bootflash/flash that is mounted within the Guest Shell.

The following sample Python script uses different CLI functions to configure and print show commands:

Device# more flash:sample_script.py


import sys
import cli

intf= sys.argv[1:]
intf = ''.join(intf[0])

print "\n\n *** Configuring interface %s with 'configurep' function  *** \n\n" %intf
cli.configurep(["interface loopback55","ip address 10.55.55.55 255.255.255.0","no shut","end"])

print "\n\n *** Configuring interface %s with 'configure' function  *** \n\n"
cmd='interface %s,logging event link-status ,end' % intf
cli.configure(cmd.split(','))

print "\n\n *** Printing show cmd with 'executep' function  *** \n\n"
cli.executep('show ip interface brief')

print "\n\n *** Printing show cmd with 'execute' function  *** \n\n"
output= cli.execute('show run interface %s' %intf)
print (output)

print "\n\n *** Configuring interface %s with 'cli' function  *** \n\n"
cli.cli('config terminal; interface %s; spanning-tree portfast edge default' %intf)

print "\n\n *** Printing show cmd with 'clip' function  *** \n\n"
cli.clip('show run interface %s' %intf)


To run a Python script from the Guest Shell, execute the guestshell run python /flash/script.py command
at the device prompt.
The following example shows how to run a Python script from the Guest Shell:



The following example shows how to run a Python script from the Guest Shell:


Device# guestshell run python /flash/sample_script.py loop55

 *** Configuring interface loop55 with 'configurep' function  ***

Line 1 SUCCESS: interface loopback55
Line 2 SUCCESS: ip address 10.55.55.55 255.255.255.0
Line 3 SUCCESS: no shut
Line 4 SUCCESS: end

 *** Configuring interface %s with 'configure' function  ***


 *** Printing show cmd with 'executep' function  ***

Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  unassigned      YES NVRAM  administratively down down
GigabitEthernet0/0     192.0.2.1       YES NVRAM  up                    up
GigabitEthernet1/0/1   unassigned      YES unset  down                  down
GigabitEthernet1/0/2   unassigned      YES unset  down                  down
GigabitEthernet1/0/3   unassigned      YES unset  down                  down
   	:
         :
         :
Te1/1/4                unassigned      YES unset  down                  down
Loopback55             10.55.55.55     YES TFTP   up                    up
Loopback66             unassigned      YES manual up                    up


 *** Printing show cmd with 'execute' function  ***

Building configuration...
Current configuration : 93 bytes
!
interface Loopback55
 ip address 10.55.55.55 255.255.255.0
 logging event link-status
end

 *** Configuring interface %s with 'cli' function  ***

 *** Printing show cmd with 'clip' function  ***

Building configuration...
Current configuration : 93 bytes
!
interface Loopback55
 ip address 10.55.55.55 255.255.255.0
 logging event link-status
end

Supported Python Versions

Guest Shell is pre-installed with Python Version 2.7. Guest Shell is a virtualized Linux-based environment, designed to run custom Linux applications, including Python applications for automated control and management of Cisco devices. Platforms with Montavista CGE7 support Python Version 2.7.11, and platforms with CentOS 7 support Python Version 2.7.5.

The following table provides information about Python versions and the supported platforms:
Table 1. Python Version Support

Python Version


Platform




Platforms with CentOS 7 support the installation of Redhat Package Manager (RPM) from the open source repository.
Updating the Cisco CLI Python Module

The Cisco CLI Python module and EEM module are pre-installed on devices. However, when you update the Python version by using either Yum or prepackaged binaries, the Cisco-provided CLI module must also be updated.
Note

When you update to Python Version 3 on a device that already has Python Version 2, both versions of Python exist on the device. Use one of the following IOS commands to run Python:

    The guestshell run python2 command enables Python Version 2.

    The guestshell run python3 command enables Python Version 3.

    The guestshell run python command enables Python Version 2.

Use one of the following methods to update the Python version:

    Standalone tarball installation

    PIP install for the CLI module

Additional References for the CLI Python Module
Related Documents
Related Topic 	Document Title

Guest Shell


Guest Shell

EEM Python Module


Python Scripting in EEM
Technical Assistance
Description 	Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.


http://www.cisco.com/support
Feature Information for the CLI Python Module

The following table provides release information about the feature or features described in this module. This table lists only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise, subsequent releases of that software release train also support that feature.
Use Cisco Feature Navigator to find information about platform support and Cisco software image support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.
Table 2. Feature Information for the CLI Python Module

Feature Name


Release


Feature Information
CLI Python Module

Cisco IOS XE Everest 16.5.1a


Python programmabilty provides a Python module that allows users to interact with IOS using CLIs.

In Cisco IOS XE Everest 16.5.1a, this feature was implemented on the following platforms:

    Cisco Catalyst 3650 Series Switches

    Cisco Catalyst 3850 Series Switches

    Cisco Catalyst 9300 Series Switches

    Cisco Catalyst 9500 Series Switches

In Cisco IOS XE Everest 16.5.1b, this feature was implemented on the following platforms:

    Cisco 4000 Series Integrated Services Routers

Cisco IOS XE Everest 16.6.2


This feature was implemented on Cisco Catalyst 9400 Series Switches.

Cisco IOS XE Fuji 16.7.1


This feature was implemented on the following platforms:

    Cisco ASR 1000 Aggregation Services Routers

    Cisco CSR 1000v Series Cloud Services Routers

Back to Top
Was this Document Helpful?
FeedbackFeedback
Contact Cisco

    Open a Support Caselogin required
    (Requires a Cisco Service Contract)

Related Cisco Community Discussions

    Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1)

    Last Reply 5 months ago

    in Unified Communications Infrastructure
    Third party optics support C9407R IOS XE Fuji 16.9.1

    Last Reply 1 year ago

    in Switching
    Cisco ASR-920-24SZ-M IOS XE UPGRADE PROCESS

    Last Reply 1 week ago

    in Routing
