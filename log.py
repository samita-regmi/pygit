
import zlib
import hashlib
import json
import os
def log():
    with open(".pygit/HEAD","r") as f:
        sha1 = f.read()
    while sha1:
        with open(".pygit/Objects/"+sha1,"rb") as f:
            compressed = f.read().strip()
        decompressed = zlib.decompress(compressed).decode()
        commit = json.loads(decompressed)
        print("commit:", sha1)
        print("author:", commit["author"])
        print("date:", commit["date"])
        print("message:", commit["message"])
        print("---")
        sha1 = commit["parent"]

