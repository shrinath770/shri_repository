import os

fo = open("shri1.txt", "r+")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
position = fo.tell()
print ("Current file position : ", position)
str = fo.read(10)
print ("Read String is : ", str)
print('"""""""""""""""""""""""""')
position = fo.seek(10, 0)
str = fo.read(10)
print ("Again read String is : ", str)
print ("Current file position : ", position)
#os.rename( "shri.txt", "shri1.txt" )
fo.close()

