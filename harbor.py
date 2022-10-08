import ipaddress
import argparse

from harbor.networking import Networking


def main():
    parser = argparse.ArgumentParser(description="Portscanner")
    parser.add_argument('-i', '--ip', required=True, type=str,
                        default=None, dest="ip",
                        help="Specify IP address or IP range to scan.")
    parser.add_argument('-p', '--ports', nargs="+", required=True, type=int,
                        default=None, dest="ports",
                        help='Specify ports to scan (E.g. 22 80 443)')
    parser.add_argument('-t', '--type', required=True, type=str,
                        default="tcp", dest="scan_type",
                        help='Specify protocol (i.e. "tcp" or "udp")')
    parser.add_argument("--pdf", required=False, type=str,
                        default=None, dest="pdf",
                        help='Specify PDF report name')
    parser.add_argument("--html", required=False, type=str,
                        default=None, dest="html",
                        help='Specify HTML report name')

    args = parser.parse_args()

    ip_range = ipaddress.ip_network(args.ip)
    network = Networking(ip_range, args.ports)
    network.do_scan("tcp")


if __name__ == '__main__':
    main()
