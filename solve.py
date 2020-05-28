from pwn import *

def makeproc(this_turn):
    path = "../rock-scissor-paper/rock-scissor-paper"
    p = process(path)
    p.recvuntil("Paper:")
    p.sendline(this_turn)
    return p

win_str = ""
for _ in range(1000):
    for _ in range(3):
        p = makeproc('r')
        if b'WON' in p.recvuntil(b"Paper:"):
            win_str += 'r'
            break
        p = makeproc('p')
        if b'WON' in p.recvuntil(b"Paper:"):
            win_str += 'p'
            break
        p = makeproc('s')
        if b'WON' in p.recvuntil(b"Paper:"):
            win_str += 's'
            break

print(win_str)
