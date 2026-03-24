with open ("sample.txt")as f:
    print(f.read())



# another way to use with but storing the result to a variable or say attribute

with open ("sample.txt")as f:
 data=(f.read())
 print(data)

#  no need to close the file as with function automatically closes file which meAns we don;t have t wory about anything to close there