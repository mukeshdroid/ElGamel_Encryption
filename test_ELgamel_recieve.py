import time
from Elgamel.keygen import keyGen
from Elgamel.lib import intEncodingLen, charEncodingLen, num2string, string2num
from Elgamel.encrypt import encrypt_msg, encrypt, encrypt_msg_numerical
from Elgamel.decrypt import decrypt_msg, decrypt, decrypt_msg_numerical

blocksize = 4

cipher = "COFYPBTWXJR MQIGBQSTWTENRMAZNRDYTKLGQHIGWEJPJCLIZROLWWOM Q YAB"

my_private_key = (8191, 17, 1672, 6788)

recovredmsg = decrypt_msg(cipher, my_private_key,blocksize)


print(recovredmsg)
