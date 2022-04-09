
def admincmd(root_lr_user=None, cmd=None):

    if cmd is None:
        return {"status" : "error", "output" : "No command specified"}

    if root_lr_user is None:
        return {"status" : "error", "output" : "root-lr user not specified"}

    status = "success"

    # Set up the AAA_USER environment variable to set up
    # task map for admin cmd execution
    export_aaa_user="export AAA_USER="+root_lr_user

    # Source ztp_helper.sh ZTP Bash library to make sure that
    # the xrcmd bash command is available

    source_ztp_bash="source /pkg/bin/ztp_helper.sh"

    # Combine the two shell commands
    cmd_env_setup=export_aaa_user+ "&&" +source_ztp_bash


    # Set up use of xrcmd and echo to funnel in admin commands
    # to the admin shell of IOS-XR
    run_admin_cmd="echo -ne \""+cmd+"\\n \" | xrcmd \"admin\""

    #Set up the final bash command to run
    cmd = cmd_env_setup+ "&&" +run_admin_cmd


    # Utilize SubProcess to run the shell command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()


    # Filter out invalid admin exec/show commands and construct list out of output

    if process.returncode:
        status = "error"
        output = "Failed to get command output"
    else:
        output_list = []
        output = ""

        for line in out.splitlines():
            fixed_line= line.replace("\n", " ").strip()
            output_list.append(fixed_line)
            if "syntax error: expecting" in fixed_line:
                status = "error"
            output = filter(None, output_list)    # Removing empty items

    # Return the result with status and output
    return {"status" : status, "output" : output}
