from run_admin_cmd import admincmd

result = admincmd(root_lr_user="admin", cmd="show platform")
from pprint import pprint
pprint(result)
