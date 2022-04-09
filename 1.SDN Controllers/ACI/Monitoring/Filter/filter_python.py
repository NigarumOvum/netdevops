"""
Simple application that logs on to the APIC and displays all
of the filters.
"""
import sys
import acitoolkit.acitoolkit as ACI


def main():
    """
    Main execution routine

    :return: None
    """
    # Take login credentials from the command line if provided
    # Otherwise, take them from your environment variables file ~/.profile
    description = 'Simple application that logs on to the APIC and displays \
                   all of the filters.'
    creds = ACI.Credentials('apic', description)
    args = creds.get()

    # Login to APIC
    session = ACI.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    # Download all of the tenants
    template = '{0:20} {1:20}'
    print template.format("TENANT", "FILTER")
    print template.format("------", "------")
    tenants = ACI.Tenant.get(session)
    for tenant in tenants:
        filters = ACI.Filter.get(session, tenant)
        for filter in filters:
            print template.format(tenant.name, filter.name)

if __name__ == '__main__':
    main()
