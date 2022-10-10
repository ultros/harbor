# harbor

#### $ python3 harbor.py -i "192.168.1.1" -p 22 443 80 -t "tcp"

    [+] Database (databases/harbor.db) loaded successfully.
    [+] Building socket list...  
    [+] 3 entries in socket list.  
    192.168.1.1:443  
    192.168.1.1:80  
    [+] Scan completed (3 of 3)  
    [+] Records written to database.  


#### $ python3 harbor.py -i "192.168.1.0/24" -p 22 443 80 -t "tcp"  

    [+] Database (databases/harbor.db) loaded successfully.
    [+] Building socket list...
    [+] 762 entries in socket list.
    192.168.1.1:443
    192.168.1.2:443
    192.168.1.1:80
    192.168.1.2:80
    [+] Scan completed (762 of 762)
    [+] Records written to database.  

