class filemgr:
    def __init__(self, fn, md):
        self.fp = open(fn, md)
    
    def __enter__(self):
        return self.fp
    
    def __exit__(self, type, value, traceback):
        self.fp.close()
    
with filemgr("file1.txt", "r+") as file:
    print(file.read())
