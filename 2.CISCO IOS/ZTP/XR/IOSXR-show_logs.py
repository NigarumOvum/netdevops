\cmd={"exec_cmd" : "show logging"}
show_logging=ztp_obj.xrcmd(cmd)

pprint (show_logging["status"])

pprint(show_logging["output"][-10:])
