# firedrill

## Let's break and learn

- Binaries are compiled using pyinstaller

### Instructions to run the Binary:

- Config file
    - Update the config file as per your environment, and keep under location `/home/yugabyte/firedrill/config.txt`
    - Sample config file:

        ```
        [global]
        server1_ip = 10.212.0.50
        server2_ip = 10.212.0.51
        server3_ip = 10.212.0.52
        key_path = /opt/yugabyte/yugaware/data/keys/26183b50-dec2-458a-ac03-27f8a9b2d95f/yb-dev-gcp_26183b50-dec2-458a-ac03-27f8a9b2d95f-key.pem 
        ssh_port = 54422
        install_path = /home/yugabyte/tserver/bin
        tls_path = /home/yugabyte/yugabyte-tls-config/
        ```

- Run the binary from YB platform server from yugabyte user
    ```
    ./<binary name>
    ```

- Create test env as per config. It expect a YB cluster with 3 nodes (each node has 1 tserver and 1 master server) and RF 3.

### Development Environment specification:

- Operating System:

    ```bash
    $ uname -r
    4.18.0-372.26.1.el8_6.x86_64
    $ cat /etc/redhat-release
        AlmaLinux release 8.6 (Sky Tiger)
    ```

- python 3.9

- pip modules installed and version:
    ```
    pyinstaller==5.4.1
    pyinstaller-hooks-contrib==2022.10
    paramiko==2.11.0
    configparser==5.0.2
    ```


- pyinstaller
    - Create the binary with -F option to include required module as well in the binary

    ```
    $ pyinstaller Exercise1.py -F
    ```
    - This will create the binary "Exercise1" in "dist" sub-folder