#FILE HANDLING
import os

with open ("example.txt",'r') as file:
    content=file.read()
    print(content)




with open ("example.txt",'r') as file :
   for line in file:
       print(line)
##.strip() is for removing spaces when we printing the lines from the content
#removes the new lne character


with open("example.txt","w") as file:
    file.write("Hello world")
    file.write("this is a new line")
    print("done")


with open("example.txt",'a') as file:
    file.write("this is a new line1")



### writing ht elist of lines to a file

lines=["\nfirst line\n","second line\n","third line\n"]
with open("example.txt","a") as file:
    file.writelines(lines)
    print("done") 


##binary files

data=b'\x00\x01\x02\x03\x04'
with open("example.bin",'wb') as file :#write byte
    file.write(data)
    print("bindone")


with open("example.bin",'rb') as file :
    content=file.read()
    print(content)


## read the content from a source content text file amd write a destination text file

with open('example.txt','r') as source_file:
    content=source_file.read()

with open ("destination.txt",'w') as destiantion_files:
    destiantion_files.write(content)

with open("example.txt","w+") as file:
    file.write("hello world")
    file.write("this is a new line aryaman")

#move the file cursor to the begining 
    file.seek(0)
    content=file.read()

    print(content)
