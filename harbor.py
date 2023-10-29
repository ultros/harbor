#!/usr/bin/env python3

import ipaddress
import argparse
import os
import pathlib
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
    parser.add_argument('-t', '--type', required=False, type=str,
                        default="tcp", dest="scan_type",
                        help='Specify protocol (i.e. "tcp" or "udp")')

    args = parser.parse_args()

    #db_path = f"{pathlib.Path(os.readlink(__file__)).parent}/databases/harbor.db"
    db_path = f"{pathlib.Path().absolute()}/databases/harbor.db"
    print(db_path)

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

    if args.scan_type.lower() == 'tcp':
        scanner = TcpScanner(ip_range, args.ports)

    if args.scan_type.lower() == 'udp':
        scanner = UdpScanner(ip_range, args.ports)


if __name__ == '__main__':
    main()
