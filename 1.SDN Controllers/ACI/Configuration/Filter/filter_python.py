"""
It logs in to the APIC and will create the filter under tenant.
"""
import acitoolkit.acitoolkit as aci

# Define static values to pass (edit these if you wish to set differently)
DEFAULT_TENANT_NAME = 'test_tenant'
DEFAULT_FILTER_NAME = 'test_filter'


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
    creds.add_argument('-f', '--filter', help='The name of contract',
                       default=DEFAULT_FILTER_NAME)
    args = creds.get()

    # Login to the APIC
    session = aci.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')

    # Create the Tenant
    tenant = aci.Tenant(args.tenant)
        
    # Create Filter
    filter = aci.Filter(args.filter, tenant)
    
    entry1 = aci.FilterEntry(args.filter,
                         applyToFrag='no',
                         arpOpc='unspecified',
                         dFromPort='3306',
                         dToPort='3306',
                         etherT='ip',
                         prot='tcp',
                         sFromPort='1',
                         sToPort='65535',
                         tcpRules='unspecified',
                         parent=filter)
    
    # Push the Contract to the APIC
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

