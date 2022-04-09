URL = 'https://sandboxapicdc.cisco.com'
LOGIN = 'admin'
PASSWORD = 'ciscopsdt'

from credentials import *
from acitoolkit import acitoolkit

# connect to the apic
session = acitoolkit.Session(URL, LOGIN, PASSWORD)
session.login()

# Create a Variable for your Tenant Name
# Use your initials in the name
# Example: "tenant_name = "js_Toolkit_Tenant""
tenant_name = "INITIALS_Toolkit_Tenant"
# create a new tenant
new_tenant = acitoolkit.Tenant(tenant_name)

# commit the new configuration
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
