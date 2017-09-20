from Crypto.Cipher import AES
import base64,os

def en(pi):
    bs=16
    padding='{'
    pad=lambda s:s+(bs-len(s)% bs)*padding
    ea=lambda  c, s:base64.b64encode(c.encrypt(pad(s)))

    secret='*ujIP)975%$3#l,]j*g!2@5^'


    cipher=AES.new(secret)
    encoded=ea(cipher,pi)
    return encoded
def dec(es):
    padding='{'
    da=lambda c,e:c.decrypt(base64.b64decode(e)).rstrip(padding)
    key='*ujIP)975%$3#l,]j*g!2@5^'
    cipher=AES.new(key)
    decoded=da(cipher,es)
    return decoded
