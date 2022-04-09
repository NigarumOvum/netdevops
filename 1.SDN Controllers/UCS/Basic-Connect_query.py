from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("<ucs-manager-ip>", "admin", "passsword")
handle.login()

#Use the vars() function to view the new handle object, and view the various properties and attributes of this class.

#    This will display the session information, for example
#        UCS Domain name
#        User Privileges
#        Session Cookie
#        Cookie refresh period

vars(handle.ip, handle.ucs, handle.cookie)

# To query all the objects of Class ID computeBlade use this python statement

handle.query_classid("computeBlade")

# All the objects that are class type computeBlade have been retrieved into memory.
# What we really need to do is retrieve the objects into a variable. Use these python statements.

blades = handle.query_classid("computeBlade")
print(blades)

# Items in a python list can be accessed a number of ways.
# For example, you can iterate over them or access directly by an object's list index.
# In this example you will iterate over the blades list and printout the object at each index.
# Use these python statements.

for blade in blades:
  print(blade)

# That resulted in quite a lot of output, each blade object's attributes and their values were printed.
# Perhaps you only want to see the blade's Dn (Distinguished Name), its number of CPUs and its available memory.
# Use these python statements.

for blade in blades:
  print(blade.dn. blade.num_of_cpus, blade.available_memory)

#Log out

handle.logout()
