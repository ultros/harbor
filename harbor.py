#!/usr/bin/env python3

import ipaddress
import argparse
import os
import re
from harbor.networking import TcpScanner, UdpScanner
from harbor.databaseutilities import DatabaseUtilities


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

    args = parser.parse_args()

    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path + '/databases/harbor.db')

    dbu = DatabaseUtilities(db_path)  # create database if it does not exist
    dbu.connect_database()
    if os.path.exists(db_path):
        try:
            dbu.create_table()
        except Exception as e:
            if re.findall("exists", str(e)):
                pass
    print(f"[+] Database (databases/harbor.db) loaded successfully.")

    ip_range = ipaddress.ip_network(args.ip)

    if args.scan_type == 'tcp':
        scanner = TcpScanner(ip_range, args.ports)

    if args.scan_type == 'udp':
        scanner = UdpScanner(ip_range, args.ports)


if __name__ == '__main__':
    main()
