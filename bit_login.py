#!/usr/bin/env python3
import requests
import time
import os
import socket
import sys

# 查询本机ip地址
def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def login(username, password,ip):
    postdata = { 'username': username,
                 'password': password,
                 'action': 'login',
                 'ipv6':'',
                 'ac_id': '1',
                 'user_ip':ip,     # 主机ip地址
                 'nas_ip':'',
                 'user_mac':'',
                 'url':'' }
    ret = requests.post('http://10.0.0.55/srun_portal_pc.php?ac_id=8',data = postdata)
    return ret
    

def main():
    username=sys.argv[1]
    password=sys.argv[2]
    ip = get_host_ip()
    if ip:
        ret = login(username, password,ip)
        print(ret)
    else :
        print('cannot get host ip')

if __name__ == '__main__':
    main()


