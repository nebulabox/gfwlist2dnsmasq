import ipaddress

# read china_ip_list.txt 
cidrs = open("china_ip_list.txt", "r")
cidr = cidrs.readline()
for cidr in cidrs:
    net=ipaddress.ip_network(cidr.strip())
    # print(cidr.strip())
    s = str(net[0]) + "-" + str(net[-1]) + ";"
    print( s ) 
cidrs.close()
