import hashlib
import zlib

def add(filepath):
    with open (filepath,"rb") as f:
        content = f.read()
    sha1 = hashlib.sha1(content).hexdigest()
    compressed = zlib.compress(content)

    with open(".pygit/objects/"+sha1, "wb") as f:
        f.write(compressed)

    with open(".pygit/index","a") as f:
        f.write(filepath+" " + sha1 + "\n")