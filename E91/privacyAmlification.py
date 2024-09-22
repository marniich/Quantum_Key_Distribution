import numpy as np
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256

def generate_random_matrix(rows, cols):
    return np.random.randint(0, 2, (rows, cols))

def generate_hash_family(output_length, key_length, family_size):
    return [generate_random_matrix(output_length, key_length) for _ in range(family_size)]

def universal_hash_with_index(weak_key, H):
    weak_key_vector = np.array([int(bit) for bit in weak_key])
    hashed_key_vector = np.mod(H @ weak_key_vector, 2)
    hashed_key_bytes = bytes(np.packbits(hashed_key_vector))
    return hashed_key_bytes

def secure_hash_using_hmac(key, data):
    h = HMAC.new(key, digestmod=SHA256)
    h.update(data)
    return h.hexdigest()
