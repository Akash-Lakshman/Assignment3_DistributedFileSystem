# Assignment3_DistributedFileSystem
Design and implementation of distributed file system

# PreRequisites

>> Python, Python Terminal, web.py

# Distributed File System 

>> Fileserver

>> NameServer

>> Client

>> Locking Service.. Not implemented

# Execution

>> Download the repository Assignment3_DistributedFileSystem.

>> In a python terminal run python nameTest.py 8000 from the python terminal. 
For file server use fileTest.py 8002 and notify the directory server.
Then clientTest.py 8003.. Make sure the ports are used in this order.

you can kill -9 a {file,lock,name}server, it will restart in the same state as when it was killed

# Working 
>> REST api Config files - to hold the server configurations (JSON files) The Directory Service automatically discovers File servers when they contact the server at startup. 
Locking Service Not working. 
