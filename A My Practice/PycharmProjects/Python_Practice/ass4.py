str1 = input("Enter String1: ")
str2 = input("Enter String2: ")

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")


#str1 = input("Enter String1: ")
#str2 = input("Enter String2: ")
#def split_str(s):
 # return [ch for ch in s]

#strArray1, strArray2, flag = split_str(str1), split_str(str2), False

#for i in strArray1:
#   for j in strArray2:
 #       if i == j:
#           flag = True

#if flag:
#    print("Strings are anagrams")
#lse:
#    print("Strings are not anagrams")