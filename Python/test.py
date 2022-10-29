x = "Hello"

def ChangeString(index, string):
    wordList = []
    for i in string:
        wordList.append(i)
    wordList.pop(index)
    wordList.insert(index, string)
    
x.ChangeString(2, "j")