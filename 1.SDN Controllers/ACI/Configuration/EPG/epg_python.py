"""
It logs in to the APIC and will create EPG in application profile under tenant
"""
import acitoolkit.acitoolkit as aci

# Define static values to pass (edit these if you wish to set differently)
DEFAULT_TENANT_NAME = 'test_tenant'
DEFAULT_APP_NAME = 'test_app'
DEFAULT_EPG_NAME = 'test_epg'
DEFAULT_BD_NAME = 'test_bd'
DEFAULT_CONTRACT_NAME = 'test_contract'


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
    creds.add_argument('-a', '--app', help='The name of application profile',
                       default=DEFAULT_APP_NAME)
    creds.add_argument('-e', '--epg', help='The name of EPG',
                       default=DEFAULT_EPG_NAME)
    creds.add_argument('-b', '--bd', help='The name of bridge domain',
                       default=DEFAULT_BD_NAME)
    creds.add_argument('-c', '--contract', help='The name of contract',
                       default=DEFAULT_CONTRACT_NAME)
    args = creds.get()

    # Login to the APIC
    session = aci.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')

    # Create the Tenant
    tenant = aci.Tenant(args.tenant)

    # Create the Application Profile
    app = aci.AppProfile(args.app, tenant)

    # Create the EPG
    epg = aci.EPG(args.epg, app)
    
    # Create the Bridge Domain
    bd = aci.BridgeDomain(args.bd, tenant)
    
    epg.add_bd(bd)
    
    # Create Contract
    contract = aci.Contract(args.contract, tenant)
    
    # Provide the contract from 1 EPG and consume from the other
    epg.provide(contract)
    epg.consume(contract)
    
    # Push the Application Profile EPG to the APIC
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

