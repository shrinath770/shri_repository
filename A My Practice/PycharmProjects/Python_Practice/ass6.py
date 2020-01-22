sentence = input("Enter sentence: ")
strarr, result = sentence.split(),[]
#print(strarr)
newWords = [word[::-1] for word in strarr[::-1]]
result = " ".join(newWords)

print(result)