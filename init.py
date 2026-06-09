import os

def init():
    os.makedirs(".pygit/objects",exist_ok = "True")
    with open(".pygit/HEAD","w") as f1:
        f1.write("")
    with open(".pygit/index","w") as f2:
        f2.write("")
    print("Initialized empty Pygit repository")