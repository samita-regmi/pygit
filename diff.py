import os
import json
import zlib
import hashlib
import difflib

def diff(filename):
    with open(filename,"r") as f:
        content = f.readlines()
    
    with open(".pygit/HEAD","r") as f:
        sha1 = f.read().strip()
    
    if not sha1:
        print("No commits yet!")
        return
    
    with open(".pygit/objects/"+sha1,"rb") as f:
        data=json.loads(zlib.decompress(f.read()).decode())

    file_hash=None
    for line in data["files"]:
        parts = line.split(" ")
        if parts[0] == filename:
            file_hash = parts[1]
            break
    
    if not file_hash:
        print(f"{filename} is not tracked")
        return

    with open(".pygit/objects/" + file_hash, "rb") as f:
        old_content = zlib.decompress(f.read()).decode().splitlines(keepends=True)
    
    diff_result = difflib.unified_diff(
        old_content,
        content,
        fromfile="old/" + filename,
        tofile="new/" + filename
    )

    printed = False
    for line in diff_result:
        print(line)
        printed = True

    if not printed:
        print(f"No changes in {filename}")