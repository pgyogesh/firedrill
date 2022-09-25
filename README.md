# firedrill

Let's break and learn

Binaries are compiled using pyinstaller 
All binaries are located in dist folder

Instructions to run the Binary:

1) Config file -- Update the config file as per your environment, and keep under location 
/home/yugabyte/firedrill/config.txt

2) Run the binary from YB platform server from yugabyte user
./<binary name>

3) Create test env as per config. It expect a YB cluster with 3 nodes (each node has 1 tserver and 1 master server) and RF 3.

Development Environment specification:

1) OS

#uname -r
4.18.0-372.26.1.el8_6.x86_64
#cat /etc/redhat-release
AlmaLinux release 8.6 (Sky Tiger)

2) python 3.9

3) pip modules installed and version:

altgraph                  0.17.2
gevent                    21.12.0
greenlet                  1.1.3
parallel-ssh              2.12.0
pip                       20.2.4
pyinstaller               5.4.1
pyinstaller-hooks-contrib 2022.10
setuptools                50.3.2
ssh-python                0.10.0
ssh2-python               1.0.0
zope.event                4.5.0
zope.interface            5.4.0

4) pyinstaller

Create the binary with -F option to include required module as well in the binary

$pyinstaller Exercise1.py -F

This will create the binary "Exercise1" in "dist" sub-folder
