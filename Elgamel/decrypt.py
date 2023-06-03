from .lib import string2Blocks, num2string, string2num, modulo_inv


def decrypt(c, private_key):
    q, g, h, x = private_key
    c1, c2 = c
    c1 = int(c1)
    c2 = int(c2)
    s = pow(c1, x, q)
    s_inv = pow(s, -1, q)
    m = (c2*s_inv) % q
    return m


def decrypt_msg(ciphertext, privatekey, blocksize, numbytes):
    li = []
    for i in range(0, len(ciphertext), blocksize):
        byte = b''.join([ciphertext[i+l].encode("ISO-8859-1")
                        for l in range(blocksize)])
        li.append(int.from_bytes(byte, "big"))
    it = iter(li)
    tokens_tuple = list(zip(it, it))
    li = []
    for token in tokens_tuple:
        li.append(decrypt(token, privatekey))
    s = ''
    for i in li:
        num = int(i).to_bytes(numbytes, 'big')
        s = s + num.decode("ISO-8859-1")
    return s


def decrypt_msg_numerical(cipher, privatekey, blocksize):
    li = []
    for token in cipher:
        li.append(decrypt(token, privatekey))
    return li


def decrypt_msg(ciphertext, privatekey, blocksize):
    numstr = str(string2num(ciphertext))

    if len(numstr) % (blocksize) != 0:
        numstr = numstr.zfill(((len(numstr) // blocksize) + 1) * blocksize)

    li = string2Blocks(numstr, blocksize)
    it = iter(li)
    tokens_tuple = list(zip(it, it))
    rs = []
    for token in tokens_tuple:
        rs.append(str(decrypt(token, privatekey)).zfill(blocksize - 1))
    s = ''.join(rs)
    return num2string(int(s))
