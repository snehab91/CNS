import hashlib
str="abcd"
result=hashlib.sha1[str.encode()]
print(result.hexdigest())