# xscript/kvfile.py
# key-value file read and write

class ReadKVFile():

    def __init__(self, name):
        self.kvfile = open(name, 'r+')
        self.kv = {}

    def read(self):
        self.kv = {}
        for line in self.kvfile.readlines():
            line = line.strip()
            if line == '':
                pass
            elif line[0] == '#':
                pass
            else:
                k, v = line.split(':', 1)
                k, v = k.strip(), v.strip()
                self.kv[k] = v

    def close(self):
        self.kvfile.close()
