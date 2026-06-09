import sys
from init import init
from add import add
from commit import commit
from log import log
from checkout import checkout
from status import status
from diff import diff

command = sys.argv[1]

if command == "init":
    init()
elif command == "add":
    filename = sys.argv[2]
    add(filename)
elif command == "commit":
    message = sys.argv[3]
    commit(message)
elif command =="log":
    log()
elif command == "checkout":
    short_hash = sys.argv[2]
    checkout(short_hash)
elif command == "status":
    status()
elif command == "diff":
    filename = sys.argv[2]
    diff(filename)