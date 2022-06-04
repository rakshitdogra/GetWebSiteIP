import socket as s 

my_hostname = s.gethostname()

print('Your Hostname is: ' + my_hostname)

my_ip = s.gethostbyname(my_hostname)


host = 'rakshitdogra.github.io'

ip = s.gethostbyname(host)

print('The IP Address of ' + host + ' is: '  + ip)