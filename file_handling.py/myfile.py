with open("doct.txt","w") as f:
    f.write("this is my first text file.\n")
    f.write("file handling.\n")
with open("doct.txt","r") as f:
    content=f.read()
    print(content)
with open("doct.txt","a") as f:
    f.write("by pooja.\n")
with open("doct.txt","r") as f:
    lines=f.readlines()
new_lines=[line.replace("handling","document") for line in lines]
with open("doct.txt","w") as f:
    f.writelines(new_lines)
with open("doct.txt","r") as f:
    content=f.read()
    print(content)
# import os
# os.remove("doct.txt")
