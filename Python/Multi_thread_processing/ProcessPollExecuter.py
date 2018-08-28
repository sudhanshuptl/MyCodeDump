# It should be used for cpu bound operations

import hashlib
from concurrent.futures import ProcessPoolExecutor


def generate_hash(text):
    return hashlib.sha3_384(text).hexdigest()


texts = [b'A quick brown fox jump over the lazy dog'
        b'The big fat panda sit on the snak'
        b'the slick mountain lion run up the tall tree']

if __name__=='__main__':
    with ProcessPoolExecutor() as executor:
        for text, hash_t in zip(texts, map(generate_hash, texts)):
            print('%s hash is %s'%(text, hash_t))