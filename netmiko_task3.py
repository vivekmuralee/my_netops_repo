from netmiko import ConnectHandler

nxosv = {'device_type': 'cisco_nxos',
        'ip': '10.0.0.6',
        'username': 'ignw',
        'password': 'ignw'}


connection = ConnectHandler(**nxosv)

command = [ 'feature interface-vlan',
            'vlan 1000',
            'interface vlan 1000',
            'description Connected to ASAv',
            'ip address 10.255.255.2 255.255.255.240',
            'no shut',
            'interface Ethernet 1/2',
            'switchport',
            'switchport mode trunk',
            'switchport trunk native vlan 1000',
            'no shut',
            'end']

config = connection.send_config_set(command)
print (config)

show_output = connection.send_command('show ip int Vlan1000 | in Vlan1000')

if show_output.count ('up') == 3:
    print ('It looks like interface VLAN1000 is "up/up"! Way to go')
else:
    print('Something went wrong .... let\'s get outa here before we break something !')
    sys.exit()


show_output = connection.send_command('show int status | in Eth1/2')

if show_output.count ('connected') == 1:
    print ('It looks like interface Ethernet1/2  is "up/up"! Way to go')
else:
    print('Something went wrong .... let\'s get outa here before we break something !')
    sys.exit()

csr = {'device_type': 'cisco_ios',
                       'ip': '10.0.0.5',
                       'username': 'ignw',
                       'password': 'ignw'}

connection = ConnectHandler(**csr)

print ('Verify Connectivity from CSR ')

command = connection.send_command('ping 10.255.255.2 source 8.8.4.4')
print (command)
