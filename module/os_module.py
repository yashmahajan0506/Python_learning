import os
print(os.getcwd())
print(os.listdir())
print(os.listdir("C:/USERS/YASHM"))
print(os.mkdir())
print(os.removedirs("parent/dir"))

os.rename("yash.txt","new.txt")
print(os.path.isfile("loops"))


path = "C:/Users/YASHM/Desktop/wann_buffer/new.txt"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.join("folder", "subfolder", "file.txt"))
print(os.path.splitext(path))


print(os.environ.get("PATH"))   
os.environ["MY_VAR"] = "123"  
print(os.environ.get("PATH"))
print(os.system("dir"))
print(os.system("ls"))

print(os.name)
print(os.getlogin())
print(os.getpid())
