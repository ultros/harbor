# harbor

#### $ python3 harbor.py -i "192.168.254.254" -p 22 443 80 -t "tcp"  

    [+] Building socket list...  
    [+] 3 entries in socket list.  
    192.168.1.1:443  
    192.168.1.1:80  
    [+] Scan completed (3 of 3)  

#### $ python3 harbor.py -i "192.168.254.0/24" -p 22 443 80 -t "tcp"  

    [+] Building socket list...
    [+] 762 entries in socket list.
    192.168.1.1:443
    192.168.1.2:443
    192.168.1.1:80
    192.168.1.2:80
    [+] Scan completed (762 of 762)
