import os
import zlib
import json

def checkout(short_hash):
    full_hash = None
    for filename in os.listdir(".pygit/objects"):
        if filename.startswith(short_hash):
            full_hash=filename
            break

    with open(".pygit/objects/"+full_hash,"rb") as f:
        decompressed = zlib.decompress(f.read()).decode()
        data = json.loads(decompressed)
    

    with open(".pygit/HEAD","r") as f:
        sha1 = f.read().strip()
    if sha1:
            with open(".pygit/objects/" + sha1, "rb") as f:
                current = json.loads(zlib.decompress(f.read()).decode())
            for line in current["files"]:
                fname = line.split(" ")[0]
                if os.path.exists(fname):
                    os.remove(fname)


    for line in data["files"]:
        parts= line.split(" ")
        filename=parts[0]
        hashname=parts[1]
    
        with open(".pygit/objects/"+hashname,"rb") as f:
            content = zlib.decompress(f.read())

        with open(filename,"wb") as f:
            f.write(content)


    with open(".pygit/HEAD", "w") as f:
        f.write(full_hash)

    print(f"Checked out to {full_hash}!")