import os
import json
import zlib
from datetime import datetime
import hashlib

def commit(message):
    with open(".pygit/index","r") as f:
        files = f.read().splitlines()
    with open(".pygit/HEAD","r") as f:
        parent = f.read().strip()
    
    commit = {
    "files": files,     
    "author": "Samita",    
    "date": str(datetime.now()),      
    "message":message ,  
    "parent": parent 
    }

    commit_data = json.dumps(commit)

    ##changing the string to bytes cus hashlib and zlib works with bytes
    
    commit_bytes = commit_data.encode()
    sha1 = hashlib.sha1(commit_bytes).hexdigest()
    compressed = zlib.compress(commit_bytes)

    with open(".pygit/objects/"+sha1, "wb") as f:
        f.write(compressed)
    

    with open(".pygit/HEAD","w") as f:
        f.write(sha1)
    
    with open(".pygit/index","w") as f:
        f.write("")
