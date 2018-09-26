from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
                       'ip': '10.0.0.5',
                       'username': 'ignw',
                       'password': 'ignw'}

connection = ConnectHandler(**cisco_cloud_router)

print (connection)
print(type(connection))

interface_Gi1  = connection.send_command('sh run interface Gi1')

print (interface_Gi1)

hostname = connection.find_prompt()
print (hostname[:-1])

interface_Gi1  = connection.send_command('sh run interface Gi1 | i ^interface')
print (interface_Gi1)
ip_interface  = connection.send_command('sh run interface Gi1 | i ip address')
if 'no' in ip_interface:
    interface_ip_address = []
    interface_ip_address[0] ='N/A'
else:
    interface_ip_address = []
    for line in ip_interface.split('\n'):
        interface_ip_address.append(line[12:])
    print (interface_ip_address)

interface_description  = connection.send_command('sh run interface Gi1 | in description')

if not interface_description:
    interface_description = 'N/A'
print (interface_description)

connection.config_mode()

config = ['interface lo0', 'description IGNW was here','ip address 172.16.1.1 255.255.255.255','no shut','end']

loopback0 = connection.send_config_set(config)
print (loopback0)

sh_lo0 = connection.send_command('sh run int lo0')
print (sh_lo0)

config = ['interface lo1', 'description IGNW was here','ip address 8.8.4.4 255.255.255.255','no shut','end']

loopback1 = connection.send_config_set(config)
print (loopback1)

sh_lo1 = connection.send_command('sh run int lo1')
print (sh_lo1)

show_output = connection.send_command('show ip int loopback1 |  in Loopback1')
if show_output.count ('up') == 2:
    print ('It looks like loopback1 is "up/up"! Way to go')
else:
    print('Something went wrong .... let\'s get outa here before we break something !')
    sys.exit()

print ('Moving to interface Gi2 .... ')

config  = ['interface Gi2',
            'ip address 203.0.113.1 255.255.255.192',
            'description This goes into the ASAv',
            'no shut',
            'end']

gigethernet2  = connection.send_config_set(config)
print (gigethernet2)

sh_Gi2 = connection.send_command('sh run int gi2')
print (sh_Gi2)

show_output = connection.send_command('show ip int GigabitEthernet2 | in GigabitEthernet2')

if show_output.count ('up') == 2:
    print ('It looks like Gigabitethernet2 is "up/up"! Way to go')
else:
    print('Something went wrong .... let\'s get outa here before we break something !')
    sys.exit()

command = ['ip route 10.255.255.2 255.255.255.255 203.0.113.2']

connection.send_config_set (command)

show_output= connection.send_command(' show ip route 10.255.255.2')
print (show_output)

if 'Network not in table' in show_output:
    print ('Something wnet wrong .... lets get out of here before we break something')
else:
    print (' Looks like the route is present')

connection.send_command('wr')
