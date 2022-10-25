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
print(server)

sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def runCommand(command):
    stdin, stdout, stderr = sshClient.exec_command(command)
    if stderr.channel.recv_exit_status() != 0:
        print("Error occurred while running exercise: " + str(stderr.read()))
        exit(1)
    else:
        return stdout.read()


def exerciseTserver1():
    print("Running exercise")
    sshClient.connect(server, port=sshPort, username='yugabyte', key_filename=keyPath, timeout=10)
    # Create Sample Table
    runCommand(postgresBinPath + 'ysqlsh -h $(hostname -i) -p 5433 -c "CREATE TABLE employee (id int) SPLIT INTO 2 TABLETS;"')
    # Insert Sample Data
    runCommand(postgresBinPath + 'ysqlsh -h $(hostname -i) -p 5433 -c "INSERT INTO employee SELECT generate_series(1,100000);"')
    # Remove the data directory
    runCommand("""curl -s $(hostname -i):7000/varz |grep fs_data_dir |awk -F'=' '{print $2"/pg_data"}' | sed 's/,/\/pg_data /g' | xargs rm -irf""")
    runCommand("""curl -s $(hostname -i):7000/varz |grep fs_data_dir |awk -F'=' '{print $2"/yb-data"}' | sed 's/,/\/yb-data /g' | xargs rm -irf""")

    # Restart the tserver
    runCommand("systemctl stop yb-tserver")
    print("We had lost the filesystem of data directory of the tserver. yb-tserver is back up and running but system is not load balanced.")
    
if __name__ == "__main__":
    exerciseTserver1()