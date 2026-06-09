import os
import json
import zlib

def status():
    staged=[]
    modified=[]
    untracked=[]

    index_files=[]
    commit_files=[]

    with open(".pygit/index","r") as f:
        content = f.read()

    with open(".pygit/HEAD","r") as f:
        sha1=f.read().strip()

    for line in content.splitlines():
        if line:
            index_files.append(line.split(" ")[0])
    
    if sha1:
        with open(".pygit/objects/"+sha1,"rb") as f:
            data=json.loads(zlib.decompress(f.read()).decode())
        
        for line in data["files"]:
            commit_files.append(line.split(" ")[0])

    for file in os.listdir("."):
        if file.endswith(".py"):
            if file in index_files:
                staged.append(file)
            elif file in commit_files:
                modified.append(file)
            else:
                untracked.append(file)


    print("Changes to be committed:")
    for f in staged:
        print("   ", f)

    print("\nChanges not staged:")
    for f in modified:
        print("   ", f)

    print("\nUntracked files:")
    for f in untracked:
        print("   ", f)

