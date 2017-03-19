
def getFileV1(filename):
    try :
        return open(filename)
    except Exception as e:
        print(e.args[1])
        return None

filename = "exception.py"
file = getFileV1(filename)
if file is not None:
    for line in file.readlines():
        pass
        #print(line)


"""
better ways with context managers that can close the file
Also catch the exception later. Especially IO errors which
signify that there is some catastrophic system level error
has happened
"""
with open("exception.py") as fileObj:
    for line in fileObj.readlines():
        print(line)


