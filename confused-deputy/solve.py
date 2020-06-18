from Crypto.Hash import SHA256

h = SHA256.new(b'apple')
print(h.hexdigest())
