"""
It logs in to the APIC and will create the bridge domain under tenant.
"""
import acitoolkit.acitoolkit as aci

# Define static values to pass (edit these if you wish to set differently)
DEFAULT_TENANT_NAME = 'test_tenant'
DEFAULT_BD_NAME = 'test_bd'
DEFAULT_SUBNET_NAME = 'test_subnet'


def main():
    """
    Main create tenant routine
    :return: None
    """
    # Get all the arguments
    description = 'It logs in to the APIC and will create the tenant.'
    creds = aci.Credentials('apic', description)
    creds.add_argument('-t', '--tenant', help='The name of tenant',
                       default=DEFAULT_TENANT_NAME)
    creds.add_argument('-b', '--bd', help='The name of bridge domain',
                       default=DEFAULT_BD_NAME)
    creds.add_argument('-s', '--subnet', help='The name of subnet',
                       default=DEFAULT_SUBNET_NAME)
    args = creds.get()

    # Login to the APIC
    session = aci.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')

    # Create the Tenant
    tenant = aci.Tenant(args.tenant)
    
    # Create the Bridge Domain
    bd = aci.BridgeDomain(args.bd, tenant)
    subnet = aci.Subnet(args.subnet, bd)
    subnet.set_addr('10.10.10.1/24')
    
    # Push the Bridge Domain to the APIC
    resp = session.push_to_apic(tenant.get_url(),
                                tenant.get_json())
    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

