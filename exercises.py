import configparser
import paramiko
import random

config = configparser.ConfigParser()
config.read('config.ini')

# Get the config section
server1 = config['global']['server1_ip']
server2 = config['global']['server2_ip']
server3 = config['global']['server3_ip']
keyPath = config['global']['key_path']
sshPort = config['global']['ssh_port']
tserverBinPath = config['global']['tserver_bin_path']
masterBinPath = config['global']['master_bin_path']
postgresBinPath = config['global']['postgres_bin_path']
tlsPath = config['global']['tls_path']
serverList = [server1, server2, server3]

# Other variables

server = random.choice(serverList)

sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def runCommand(command):
    stdin, stdout, stderr = sshClient.exec_command(command)
    if stderr.channel.recv_exit_status() != 0:
        print("Error occurred while running exercise: " + str(stderr.read()))
        exit(1)
    else:
        return stdout.read()

def exercise_1():
    print("Running Exercise")
    sshClient.connect(server, port=sshPort, username='yugabyte', key_filename=keyPath)
    runCommand(tserverBinPath + 'yb-admin --master_addresses ' + server1 + ',' + server2 + ',' + server3 + ' --certs_dir_name ' + tlsPath + ' set_load_balancer_enabled 0')
    sshClient.close()    
    print("Open the master UI")
    
def exercise_2():
    print("Running Excercise")
    sshClient.connect(server, port=sshPort, username='yugabyte', key_filename=keyPath)
    runCommand("sudo chmod -x " + tserverBinPath + "yb-tserver")
    runCommand("sudo shutdown -r now")
    print("Check health of the universe")
