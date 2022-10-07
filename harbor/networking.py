import socket


class Networking:

    def __init__(self, ips: list, ports: int):
        self._ips = ips
        self.ports = ports
        self.hostnames = []

    @property
    def ips(self) -> list:
        return self._ips

    @ips.setter
    def ips(self, new_ips: list):
        if isinstance(new_ips, list):
            self._ips = new_ips
        else:
            print("IP address(es) must be passed in a list.")

    def get_hostnames(self):
        for ip in self.ips:
            self.hostnames.append(socket.gethostbyaddr(ip))
            # update hostname record where ip address == ip

    def delete_hostnames(self):
        self.hostnames = []


class TcpPortscan(Networking):
    pass


class UdpPortscan(Networking):
    pass


class PingSweep(Networking):
    pass


class XmasTreeScan(Networking):
    pass


nw = Networking(["test", "test2", "test3"], 22)
# print(nw.ips)

tcp_port_scan = TcpPortscan(["173.236.172.84"], 22)
#print(tcp_port_scan.ips)
tcp_port_scan.get_hostnames()
print(tcp_port_scan.hostnames[0][0])



class SocksProxy:

    def __init__(self, proxy_type: str, proxy_ip: str, proxy_port: int, proxy_username: str, proxy_password: str):
        self.proxy_type = proxy_type
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password


socks = SocksProxy("asdf", "asdf", 33, "asdf", "asdf")
