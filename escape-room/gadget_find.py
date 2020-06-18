import subprocess


liblist = ["/lib/i386-linux-gnu/libxml2.so.2",
"/lib/i386-linux-gnu/libm.so.6",
"/lib/i386-linux-gnu/libdl.so.2",
"/lib/i386-linux-gnu/libicuuc.so.63",
"/lib/i386-linux-gnu/libz.so.1",
"/lib/i386-linux-gnu/liblzma.so.6",
"/lib/ld-linux.so.2",
"/lib/i386-linux-gnu/libicudata.so.63",
"/lib/i386-linux-gnu/libpthread.so.0",
"/lib/i386-linux-gnu/libstdc++.so.6",
"/lib/i386-linux-gnu/libgcc_s.so.1"]

re = "mov dword ptr \[esi\], edi"
for lib in liblist:
    print(lib)
    subprocess.run(["ROPgadget", "--re", re, "--binary", lib, "--offset", "0x0"])

#ROPgadget --re "mov dword ptr \[esi\], edi" --binary

#.init = 00075000
#.text 0007cf80
#0x00110557 : add esp, 0x20 ; mov dword ptr [esi], edi ; pop ebx ; pop esi ; pop edi ; ret
# 0x9b55a ; mov dword ptr [esi], edi; pop ebx; pop esi; pop edi; ret
