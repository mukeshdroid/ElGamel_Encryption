import time
from Elgamel.keygen import keyGen
from Elgamel.lib import intEncodingLen, charEncodingLen, num2string, string2num
from Elgamel.encrypt import encrypt_msg, encrypt, encrypt_msg_numerical
from Elgamel.decrypt import decrypt_msg, decrypt, decrypt_msg_numerical


blocksize = 4


message = 'HELLO'

start = time.perf_counter_ns()
alice_private_key, alice_public_key = keyGen(blocksize)

alice_private_key, alice_public_key = keyGen(blocksize)
cipher = encrypt_msg(message, alice_public_key, blocksize)
print(cipher)

recover = decrypt_msg(cipher, alice_private_key, blocksize)

print('message :: {} Recovered :: {}'.format(message, recover))

print("the time taken is" +
      str((time.perf_counter_ns() - start) * (1/1e9)) + "seconds")
