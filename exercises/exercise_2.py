from firedrill_lib import get_config
import subprocess

print("Running Exercise 2")

var = get_config()

for k in var:
    if ("server" in k):
        subprocess.run(['sudo', 'ssh', '-i', var["key_location"], '-ostricthostkeychecking=no', '-p', var["ssh_port"], 'ec2-user@' + var[k], 'sudo','chmod','-x',var["install_location"] + 'yb-tserver'])
        subprocess.run(['sudo', 'ssh', '-i', var["key_location"], '-ostricthostkeychecking=no', '-p', var["ssh_port"], 'ec2-user@' + var[k], 'sudo','shutdown','-r','now'])
        print ("Service is not running on one of the node. Please investigate")
    break

