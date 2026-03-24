# line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# line6=f.readline()
# print(line6,type(line6))

# line4=f.readline()
# print(line4,type(line4))

# line8=f.readline()
# print(line8,type(line8))

# f=open("myfile.txt")
# line=f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()
# f.close()


# how to open a file'
# use open function firstly to open the file
# use read function to read the file
# use print to read the file
# at last close the file

# eg
# name=open("file.txt")
# data=name.read()
# print(data)
# name.close()


#  build in function: open by default mode is r i.e. read
# write in a file

# str="the name is mad max"
# f= open("file.txt","w")
# f.write(str)
# f.close()

# st="hey harry you are amazing"
# f=open("file.txt","a")
# f.write(st)
# f.close()

#  the same can be written using with statement like this:
with open ("file.txt") as f:
    print(f.read())