"""
It logs in to the APIC and will create the vlan pool.
"""
import acitoolkit.acitoolkit as aci

# Define static values to pass (edit these if you wish to set differently)
DEFAULT_VLAN_NAME = 'test_vlan'


def main():
    """
    Main create tenant routine
    :return: None
    """
    # Get all the arguments
    description = 'It logs in to the APIC and will create the vlan pool.'
    creds = aci.Credentials('apic', description)
    creds.add_argument('-v', '--vlan', help='The name of vlan pool',
                       default=DEFAULT_VLAN_NAME)
    args = creds.get()

    # Login to the APIC
    session = aci.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')

    # Create the VLAN pool
    vlan_pool = aci.NetworkPool(args.vlan, 'vlan', '222', '223', 'dynamic')

    # Push the VLAN pool to the APIC
    resp = session.push_to_apic(vlan_pool.get_url(),
                                vlan_pool.get_json())
    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
