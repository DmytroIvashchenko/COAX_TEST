import hashlib

# MD5 хешування
s = "Python Bootcamp"

hash_object = hashlib.md5(s.encode())
print(hash_object.hexdigest())

# SHA1 хешування
hash_object = hashlib.sha1(b'Python Bootcamp')
hex_dig = hash_object.hexdigest()

print(hex_dig)
