# context manager
with open("file2.txt", "w") as fp:
    print(f"file pointer location: {fp.tell()}")
    print(f"file pointer: {fp.tell()}")