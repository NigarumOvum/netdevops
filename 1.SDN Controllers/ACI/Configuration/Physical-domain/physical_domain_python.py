"""
It logs in to the APIC and will create the physical domain.
"""
import acitoolkit.acitoolkit as aci

# Define static values to pass (edit these if you wish to set differently)
DEFAULT_PHY_DOMAIN_NAME = 'test_phy_dmn'


def main():
    """
    Main create tenant routine
    :return: None
    """
    # Get all the arguments
    description = 'It logs in to APIC and will create the physical domain.'
    creds = aci.Credentials('apic', description)
    creds.add_argument('-p', '--phy_domain', 
                       help='The name of physical domain',
                       default=DEFAULT_PHY_DOMAIN_NAME)
    args = creds.get()

    # Login to the APIC
    session = aci.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')

    # Create the physical Domain
    phy_dmn = aci.PhysDomain(args.phy_domain)

    # Push the physical domain to the APIC
    resp = session.push_to_apic(phy_dmn.get_url(),
                                phy_dmn.get_json())
    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

