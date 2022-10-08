import concurrent.futures
import socket
from ipaddress import IPv4Network


class Networking:

    def __init__(self, ips: IPv4Network, ports: list):
        self._ips = ips
        self.ports = ports
        self.hostnames = []
        self.socket_list = []

    @property
    def ips(self) -> IPv4Network:
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

    def build_socket_list(self):
        """Builds a list of IP/Port pairs (sockets)
        and returns this list.
        """
        socket_list = []

        for ip in self.ips.hosts():
            for port in self.ports:
                socket_list.append((str(ip), port))

        return socket_list

    @staticmethod
    def socket_connect(ip: str, port: int, scan_type: str):

        match scan_type:
            case "tcp":
                protocol = socket.SOCK_STREAM
            case "udp":
                protocol = socket.SOCK_DGRAM
            case _:
                '[!] Specify a protocol for scan (i.e. "tcp" or "udp")'
                exit(0)
        try:
            connection = socket.socket(socket.AF_INET, protocol)
            connection.settimeout(3.0)

            if connection.connect_ex((ip, port)) == 0:  # if connection was successful
                return ip, port

            connection.close()

        except Exception as e:
            print(e)

    def do_scan(self, scan_type: str):
        """Prepare a concurrent TCP or UDP scan against a list of IP addresses
        and port numbers.
        """

        i = 0
        print("[+] Building socket list...")
        socket_list = self.build_socket_list()
        print(f"[+] {len(socket_list)} entries in socket list.")

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = []

            for entry in socket_list:
                ip = entry[0]
                port = entry[1]
                futures.append(executor.submit(self.socket_connect, ip, port, scan_type))

            for future in concurrent.futures.as_completed(futures):
                response = future.result()
                if response is not None:
                    print(f"{response[0]}:{response[1]}")

                i += 1
                print(f"{i} out of {len(socket_list)}", end="\r")

            print(f"[+] Scan completed ({i} of {len(socket_list)})")

class SocksProxy:

    def __init__(self, proxy_type: str, proxy_ip: str, proxy_port: int, proxy_username: str, proxy_password: str):
        self.proxy_type = proxy_type
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password