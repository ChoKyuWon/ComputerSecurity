import codecs
from scapy.layers.tls.crypto.prf import PRF
""" ***** PrivKeyRSA *****
Documentation: https://scapy.readthedocs.io/en/latest/api/scapy.layers.tls.cert.html
Source Code  : https://github.com/secdev/scapy/blob/master/scapy/layers/tls/cert.py
*NOTE* There are functions not listed on the documentation page (e.g., decrypt())
"""
from scapy.layers.tls.cert import PrivKeyRSA, X509_Cert
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# Useful Parameters for scapy API
TLS_12= 0x303
PRF_ALGORITHM = "SHA256"

# Useful functions for converting between hex string and binary data in Python3
def hex_to_data(hex_str):
    return bytearray.fromhex(hex_str)

def data_to_hex(data):
    return bytearray(data).hex()

client_random = hex_to_data('50ba2c6dd9a809d3560429e5d4f36584b0120909ba76e642f012ed847d1711fe')
server_random = hex_to_data('19a75738be10c27b2206d0acd7678336ee0c1a36f13e47109df94e9a7823ecc2')

"""
Note: Your answers should be in hexadecimal strings (e.g., 'c0d295a50d66...')
"""

"""
1. Decrypt the premaster secret and print it (10 pts)
"""


# Your code goes here
encrypted_premaster_secret = '92c4684b5c1bb97aa3cd3bf8caf33cc659b1e3294d8f98618eb4f961792985ec75d18088f760db4096be2b894f5778a73e0f40b118120bd306340a158be3a770fc173977fceb7b1f1fad35f6cfbbe2efa4dcc7b4b9f798879b6ff22e190e3f75e194333e00472a7c6370425c4ef1702ed3a9166a2c27a1fe2587dc13794192cd0677b49e600e77ea153dce079ea34756bd813de352f3aeae9a09b9369cc16a79c8cd51d48bf484b08a6fc3f245812236ea10285ce347e41a93f0a398ec6f8b8b2edcd55d10fe35bb88ebbabb556d6d42544886f462bce76c1515b6ad0ed1f547cf4a1a9ba423853ffa99d174dfba8071d6808155ab4d9ac6866a472df7a77106'

privkey = open('key.pem', 'r').read()
rsakey = RSA.importKey(privkey)
rsa = PKCS1_v1_5.new(rsakey)
sentinel = 'Error'
premaster_secret = rsa.decrypt(hex_to_data(encrypted_premaster_secret), sentinel)

# Your answer should be printed here
print('Decrypted Premaster Secret: %s' % data_to_hex(premaster_secret))


"""
2. Caclulate Master Secret (20 pts)
"""

# Your code goes here
prf = PRF(hash_name=PRF_ALGORITHM, tls_version=TLS_12)
master_secret = prf.compute_master_secret(premaster_secret, client_random, server_random)
# Your answer should be printed here
print('Master Secret: %s' % data_to_hex(master_secret))

"""
3. Calculate the Following (30 pts): 


    1) Client Write Key,
    2) Client Write IV,
    3) Client Write Mac Key,
    4) Server Write Key,
    5) Server Write IV,
    6) Server Write Mac Key

Hint: KeyBlock Layout is as the following
- Byte00-Byte015: Server Write IV
- Byte16-Byte031: Client Write IV
- Byte32-Byte047: Server Write Key
- Byte48-Byte063: Client Write Key
- Byte64-Byte095: Server MAC Key
- Byte96-Byte127: Client MAC Key
"""
key_block = prf.derive_key_block(master_secret, server_random, client_random, 128)
# Your answer should be printed here
print('Key Block: %s ' % bytearray(key_block))

# Your code goes here
'''
server_write_IV = key_block[:16]
client_write_IV = key_block[16:32]
server_write_key = key_block[32:48]
client_write_key = key_block[48:64]
server_write_MAC_key = key_block[64:96]
client_write_MAC_key = key_block[96:]
'''

client_write_MAC_key = key_block[:32]
server_write_MAC_key = key_block[32:64]
client_write_key = key_block[64:80]
server_write_key = key_block[80:96]
client_write_IV = key_block[96:112]
server_write_IV = key_block[112:]


# Your answer should be printed here
print('Server Write IV: %s' % server_write_IV)
print('Client Write IV: %s' % client_write_IV)
print('Server Write Key: %s' % server_write_key)       
print('Client Write Key: %s' % client_write_key) 
print('Server Write MAC Key: %s' % server_write_MAC_key) 
print('Client Write MAC Key: %s' % client_write_MAC_key)

"""
4. Decrypt the Message, Get the Flag (40pts)
"""
flag = ''

# Your code goes here
 
Client_to_Server = 'd03ad968a9cb4663e3d2d02acdab71cc5ee5fb2e874d659561c5b459d71e5c2ca05c4f4c6f347cd0048e922be097136f500b93837c149cef32ead52ffe3c0f0d22ba543eeee3ead83cbb35a906ebf097'
Server_to_Client = 'e8c9f048fb62f3b24fbc3797754cc4387fc5ac38d0dcd911d7524528bf85abe0398a448023364ffd506dd1a01d32ead7b3b13037f17b1731428f509df91243a9489edc6badb9555ef7d9a584bfc4e5ba94da7470780bbb930997b552e1d45055ebed2c8fe973ab4e19c8bb5a5f8ae24a'

C2S_cipher = AES.new(client_write_key, AES.MODE_CBC, client_write_IV)
S2C_cipher = AES.new(server_write_key, AES.MODE_CBC, server_write_IV)

pt1 = C2S_cipher.decrypt(hex_to_data(Client_to_Server[:-32]))
pt2 = S2C_cipher.decrypt(hex_to_data(Server_to_Client[:-32]))

print(pt1)
print(pt2)
# Your answer should be printed here


# Now you can get on ctf.skku.edu and enter the flag :)
