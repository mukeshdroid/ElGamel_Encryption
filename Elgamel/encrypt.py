from random import randint
from .lib import string2Blocks, num2string, string2num


def encrypt(m, key):
    q, g, h = key
    y = randint(2, q-1)
    s = pow(h, y, q)
    c1 = pow(g, y, q)
    c2 = (m*s) % q
    return (c1, c2)


def encrypt_msg(plaintext, publickey, blocksize, numbytes):
    if len(plaintext) % blocksize != 0:
        plaintext += ' '*(plaintext % blocksize)

    li = []
    for i in range(0, len(plaintext), blocksize):
        byte = b''.join([plaintext[i+l].encode("ISO-8859-1")
                        for l in range(blocksize)])
        li.append(int.from_bytes(byte, "big"))
    nc = []
    for token in li:
        c1, c2 = encrypt(token, publickey)
        nc.append(c1)
        nc.append(c2)

    cipher = ''
    for i in nc:
        num = int(i).to_bytes(numbytes, 'big')
        cipher = cipher + num.decode("ISO-8859-1")
    return cipher


def encrypt_msg_numerical(plaintext, publickey, blocksize, key_len):
    tokens = string2Blocks(plaintext, blocksize)
    tokens_num = list(map(string2num, tokens))
    li_num = []
    for token in tokens_num:
        li_num.append(encrypt(token, publickey))
    return li_num


def encrypt_msg(plaintext, publickey, blocksize):

    numstr = str(string2num(plaintext))

    if len(numstr) % (blocksize - 1) != 0:
        nl = (len(numstr) // (blocksize - 1) + 1) * (blocksize - 1)
        numstr = numstr.zfill(nl)

    tokens = string2Blocks(numstr, blocksize-1)

    nc = []
    for token in tokens:
        c1, c2 = encrypt(int(token), publickey)
        nc.append(str(c1).zfill(blocksize))
        nc.append(str(c2).zfill(blocksize))

    cipher = ''.join(nc)
    return num2string(int(cipher))
