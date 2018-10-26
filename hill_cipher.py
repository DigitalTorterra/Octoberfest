import numpy as np

def generate_key(n):
    #nxn matrix
    key = np.random.randint(0, high=50, size=(n,n))
    return(key)
  
def prep(message, key):
    size = key.shape[0]
    message = message.split()
    message = ''.join(message)
    message = message.lower()
    number = np.ceil(np.array(len(message) / size))
    number = int(number)
    bits = [message[i*size:(1+i)*size] for i in range(number)]
    if len(bits[-1]) != size:
        num_pad = size - len(bits[-1])
        pad = ['a' for i in range(num_pad)]
        pad = ''.join(pad)
        bits[-1] += pad
    return(bits)

def letter_to_num(string):
    nums = []
    for char in string:
        nums.append('abcdefghijklmnopqrstuvwxyz'.index(char))
    return(nums)

def encode(message, key):
    bits = prep(message, key)
    new_message = []
    for bit in bits:
        vec = np.array(letter_to_num(bit))
        vec = vec.T
        code = np.matmul(key, vec)
        
    