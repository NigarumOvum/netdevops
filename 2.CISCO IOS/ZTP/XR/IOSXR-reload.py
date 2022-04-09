from run_admin_cmd import admincmd

reload_cmd="hw-module location all  reload\n yes\n"
admincmd(root_lr_user="admin", cmd=reload_cmd)
