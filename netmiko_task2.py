from netmiko import ConnectHandler

asav = {'device_type': 'cisco_asa',
        'ip': '10.0.0.8',
        'username': 'ignw',
        'password': 'ignw',
        'secret': 'ignw'}

connection = ConnectHandler(**asav)

command = ['interface GigabitEthernet0/0',
            'description Connected to CSR',
            'nameif outside',
            'security-level 0',
            'ip address 203.0.113.2 255.255.255.192',
            'no shut',
            'end']

print ('Configuration for Gi0/0')
config_Gi0_0 = connection.send_config_set(command)
print (config_Gi0_0)

command = ['interface Gi0/1',
            'description Connected to NX-OSv',
            'nameif inside',
            'security-level 100',
            'ip address 10.255.255.1 255.255.255.240',
            'no shut',
            'end']

print ('Configuration for Gig0/1')

config_Gi0_1 = connection.send_config_set(command)
print (config_Gi0_1)

show_output = connection.send_command('show int ip  brief | in GigabitEthernet0/0')

if show_output.count ('up') == 2:
    print ('It looks like Gigabitethernet0/0 is "up/up"! Way to go')
else:
    print('Something went wrong .... let\'s get outa here before we break something !')
    sys.exit()

show_output = connection.send_command('show int ip brief | in GigabitEthernet0/1')

if show_output.count ('up') == 2:
    print ('It looks like Gigabitethernet0/1 is "up/up"! Way to go')
else:
    print('Something went wrong .... let\'s get outa here before we break something !')
    sys.exit()

route_command = [ 'route outside 8.8.4.4 255.255.255.255 203.0.113.1' ]

print ('Adding static route ')

route_config  = connection.send_config_set(route_command)
print (route_config)

route = connection.send_command ('show route 8.8.4.4')
print (route)

if 'Network not in table' in route:
    print ('Something wnet wrong .... lets get out of here before we break something')
else:
    print (' Looks like the route is present')

print ('Configuring ACL')

command  = ['access-list outside_in ext permit icmp any any',
            'access-group outside_in in interface outside']
acl_config = connection.send_config_set(command)
print (acl_config)

connection.send_command('wr')
