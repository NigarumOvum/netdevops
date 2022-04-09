"""
Simple application that logs on to the APIC and displays all
of the Physical Domains.
"""
import sys
import acitoolkit.acitoolkit as aci


def main():
    """
    Main Show Physical Domains Routine
    :return: None
    """
    # Take login credentials from the command line if provided
    # Otherwise, take them from your environment variables file ~/.profile
    description = ('Simple application that logs on to the APIC'
                   ' and displays all of the Physical Domains.')
    creds = aci.Credentials('apic', description)
    args = creds.get()

    # Login to APIC
    session = aci.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    domains = aci.PhysDomain.get(session)

    if len(domains) > 0:
        print ('---------------')
        print ('Physical Domain')
        print ('---------------')

    for domain in domains:
        print domain.name

    if len(domains) > 0:
        print '\n'

    domains = aci.VmmDomain.get(session)

    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass    
