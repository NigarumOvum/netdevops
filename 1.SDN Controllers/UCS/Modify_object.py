# Exercise 1 - Query Compute and Led Objects
# Retrieve the equipmentLocatorLed operational status of each compute object, display the compute object dn and the equipmentLocatorLed oper_state. Use these python statements.

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110", "admin", "password")

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        print(compute_resource.dn, leds[0].oper_state)

# Retrieve the equipmentLocatorLed operational status of each compute object, change the oper_state to the
# opposite of the current state using the set_mo and commit methods.
# The equipmentLocatorLed state is shown via the oper_state however, the state is managed through the admin_state. Use these python statements.

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "admin", "password")

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        previous_oper_state = leds[0].oper_state

        if leds[0].oper_state == "on":
            leds[0].admin_state = "off"
        else:
            leds[0].admin_state = "on"

        handle.set_mo(leds[0])
        handle.commit()

        print( "dn:",compute_resource.dn,
               "led previous",previous_oper_state,
               "led current",leds[0].admin_state)
