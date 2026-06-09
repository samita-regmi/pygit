# PyGit 🐍

A mini version control system built from scratch using only Python's built-in tools. PyGit works similarly to Git with all the basic features you need to track changes to your project.

Built as part of my Python learning journey — and it was actually fun to make!

## Features

- Initialize a repository
- Add files to staging area
- Commit snapshots with messages
- View commit history
- Checkout previous commits

## How to Use

**Initialize a repository:**

python pygit.py init


**Add a file:**

python pygit.py add filename.py


**Commit a snapshot:**

python pygit.py commit -m "your message"


**View history:**

python pygit.py log


**Checkout a previous commit:**

python pygit.py checkout <first 6 chars of commit hash>


## How it Works

PyGit stores compressed snapshots of your files using SHA-1 hashing and zlib compression. Every commit is chained to the previous one through a parent hash — just like real Git!

## Built With

- Python (built-in libraries only!)
- hashlib
- zlib
- json
- os