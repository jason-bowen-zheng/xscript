def fileclose(fileobj):
    fileobj.close()

def fileflush(fileobj):
    fileobj.flush()

def fileopen(name, mode='r'):
    return open(name, mode)

def fileread(fileobj, size=-1):
    return fileobj.read(int(size))

def filewrite(fileobj, s):
    return fileobj.write(s)