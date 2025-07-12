# with open("file1.txt", "a") as fp:
#     print(fp.tell())
#     fp.write("\n")
#     fp.write("some things")

# with open("file1.txt", "a+") as fp:
#     print(fp.tell())
#     fp.seek(0)
#     print(fp.read())

# with open("file1.txt", "a+") as fp:
#     print(fp.tell())
#     fp.seek(0)
#     lines = fp.read()

# lines_list = lines.split("\n")
# print(lines_list)


with open("file1.txt", "a+") as fp:
    print(fp.tell())
    fp.seek(0)
    lines = fp.readlines()
    lines.append("\nhey i am a new line from python\n")
    lines.append("I am the last line")
    fp.seek(0)
    fp.truncate()
    fp.writelines(lines)

print(lines)