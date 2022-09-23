from read_file import get_config
import subprocess

var = get_config()

for k in var:
    if ("server" in k):
        subprocess.run(['sudo', 'ssh', '-i', var["key_location"], '-ostricthostkeychecking=no', '-p', var["ssh_port"], 'yugabyte@' + var[k], var["install_location"] + 'yb-admin', '--master_addresses', var["server1_ip"] + "," + var["server2_ip"] + "," + var["server3_ip"], '-certs_dir_name', var["tls_location"], 'set_load_balancer_enabled','0'])
        print ("Please check load balancer status")
    break

