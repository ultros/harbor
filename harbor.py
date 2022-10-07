import ipaddress

from harbor.networking import Networking


def main():

    ip_range = ipaddress.ip_network('142.251.33.110')
    network = Networking(ip_range, [22, 80, 443])
    network.do_scan("tcp")
    #ip_list = network.build_socket_list()

    #print(ip_list)
    # for ip in ip_range.hosts():
    #     for port in ports:
    #         print(ip, port)

if __name__ == '__main__':
    main()
