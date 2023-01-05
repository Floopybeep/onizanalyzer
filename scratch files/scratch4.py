# print(format(211, 'x').upper())
import hashlib
import time
from fnvhash import fnv1a_32

ts = time.time()
print(hash('hahahaha'))
print(time.time()-ts)

print(hashlib.sha1('hahahaha'.encode('utf-8')).hexdigest())
print(time.time()-ts)

print(fnv1a_32('hahahaha'.encode('utf-8')))
print(time.time()-ts)

