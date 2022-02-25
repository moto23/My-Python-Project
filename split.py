def remove_and_split(string,word):
    newStr = string.replace(word, "")
    return newStr.split()

this ="      Prasad Loves to Play football       "
n = remove_and_split(this)
print(n)

