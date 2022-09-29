import configparser
import paramiko
import random

config = configparser.ConfigParser()
config.read('config.ini')

# Get the config section
server1 = config['global']['server-1_ip']
server2 = config['global']['server-2_ip']
server3 = config['global']['server-3_ip']
keyPath = config['global']['key_path']
sshPort = config['global']['ssh_port']
installPath = config['global']['install_path']
tlsPath = config['global']['tls_path']
serverList = [server1, server2, server3]

# Other variables

server = random.choice(serverList)
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
def exercise_1():
    # Connect to the server
    sshClient.connect(server, port=sshPort, username='yugabyte', key_filename=keyPath)
    # Run the command
    stdin, stdout, stderr = sshClient.exec_command(installPath + 'yb-admin --master_addresses ' + server1 + ',' + server2 + ',' + server3 + ' --certs_dir_name ' + tlsPath + ' set_load_balancer_enabled 0')
    # Print the output
    print(stdout.read().decode())
    # Close the connection
    sshClient.close()    
    # Hint:
    print("Open the master UI")
    
def exercise_2():
    sshClient.connect(server, port=sshPort, username='yugabyte', key_filename=keyPath)
    stdin, stdout, stderr = sshClient.exec_command("sudo chmod -x " + installPath + "yb-tserver")
    stdin, stdout, stderr = sshClient.exec_command("sudo shutdown -r now")
    print("Check health of the universe")