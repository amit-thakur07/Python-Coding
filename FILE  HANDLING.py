# file handling and reading the files in term of a string
# read the entire file text
# f=open("file.txt","r")
# data=f.read()
# print(data)
# f.close

# read the files by using the readlines() in term of a list
# f=open("file.txt","r")
# data=f.readlines()
# print(data)
# f.close

# reading lines one by one

# f=open("file.txt","r")
# data=f.readline()
# print(data,end="")
# data1=f.readline()
# print(data1)
# f.close()


# Write mode: 1. write "w" :for overiding the whole text from the file,2."a" means to write something to the end of the text file
# f=open("file.txt","w")
# f.write("this is a cat").. it will overwrites the text file and delete the previous lines of text


# append mode = 
# f=open("file.txt","a")
# f.write("you are a lier")

# new file creation by using w and writting to it some text: 
# file=open("sample.txt","w")
# file.write("you are the new file created in w")
# file.close()

# r+ mode to overwrite the text in the given files no truncate and ptr at start works only if the n=old file exists
# a=open("file.txt","r+")
# a.write("i am the next text")
# print(a.read())
# a.close

# w+ mode truncated and can make new file do not exists
# f=open("single.txt","w+")
# f.write("i am the latest creation")
# f.seek(0)
# data =f.read()
# print(data)

# a+ read and add at the end
# f=open("single.txt","a+")
# f.write("\n ok")
# f.seek(0)
# data=f.read()
# print(data)



