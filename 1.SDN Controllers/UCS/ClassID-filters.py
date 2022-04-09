#    Log into the UCS Manager. Use these python statements.

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "admin", "passsword")
handle.login()

#    Query computeBlade and display some of each blade's attributes. Use these python statements.

blades = handle.query_classid("computeBlade")
for blade in blades:
  print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)

#    Use a filter to only Query for blades with a specific attribute equal to a value.

blades = handle.query_classid("computeBlade", filter_str="(model, 'UCSB-EX-M4-1', type='eq')")
for blade in blades:
  print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)

  # Use a filter to only Query for blades with a specific attribute using a regular expression re.

blades = handle.query_classid("computeBlade", filter_str="(dn, 'blade-[2,4,6,8]', type='re')")
for blade in blades:
  print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)\

#    Use a filter to only Query for blades with a specific attribute using a regular expression re.

blades = handle.query_classid("computeBlade", filter_str="(dn, 'blade-[2,4,6,8]', type='re')")
for blade in blades:
  print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)
