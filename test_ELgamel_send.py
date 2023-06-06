import time
from Elgamel.keygen import keyGen
from Elgamel.lib import intEncodingLen, charEncodingLen, num2string, string2num
from Elgamel.encrypt import encrypt_msg, encrypt, encrypt_msg_numerical
from Elgamel.decrypt import decrypt_msg, decrypt, decrypt_msg_numerical


blocksize = 4


message = 'NUMBER THOERY IS MY FAV'

priyanka_public_key = (8191, 17, 1672)


cipher = encrypt_msg(message, priyanka_public_key, blocksize)




print(cipher)


