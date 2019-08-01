import random, string
import hashlib
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i  in range(16))
print(x)

hash_object = hashlib.sha256('x').hexdigest()
print(hash_object)

