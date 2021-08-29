import os

#print("/".join(os.getcwd().split("/").pop()))

print("/".join(os.getcwd().split("/")[0:-1])+"/CurPos.json")