import time
from Elgamel.keygen import keyGen
from Elgamel.lib import intEncodingLen, charEncodingLen, num2string, string2num
from Elgamel.encrypt import encrypt_msg, encrypt, encrypt_msg_numerical
from Elgamel.decrypt import decrypt_msg, decrypt, decrypt_msg_numerical

blocksize = 4



my_private_key, my_public_key = keyGen(blocksize)

print(my_private_key)

print(my_public_key)