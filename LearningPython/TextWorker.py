import time
#1
def WordCount(textString):
    return textString.count(' ') + 1
#2
def RemoveGarbage(textString):
    cleanString = ""
    #for word in textString.split(" "):
    #    if word.isalpha():
    #        cleanString += word + " "

    for ch in textString:
        if ch == '\n':
                ch = ' '
        if ch == ' ' or ((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
            if ch != ' ' or cleanString[:-1] != ' ':
                cleanString += ch
    return cleanString

#3
def UniqueWordsCount(textString):
    wordSet = set()
    for word in textString.split():
        wordSet.add(word)
    return len(wordSet)
#4.1
def UniqueNotIn(textString1, textString2):
    wordSet1 = set()
    for word in textString1.split():
        wordSet1.add(word)
     
    wordSet2 = set()
    for word in textString2.split():
        wordSet2.add(word)

    return wordSet1 - wordSet2
#4.2
def UniqueNotInCount(textString1, textString2):
    return len(UniqueNotIn(textString1, textString2))

#5
def UniqueSame(textString1, textString2):
    wordSet1 = set()
    for word in textString1.split():
        wordSet1.add(word)
     
    wordSet2 = set()
    for word in textString2.split():
        wordSet2.add(word)

    return wordSet1 & wordSet2

#6
def Alphabet(textString):
    wordSet = set()
    for word in textString.split(" "):
        wordSet.add(word)
    return sorted(wordSet)

words = []
wordTemplate = ''
with open('text1.txt') as f:
    for ch in f.read():
        if ch == ' ':
            if len(wordTemplate) > 0:
                words.append(wordTemplate)
            wordTemplate = ''


text2 = ''
with open('text2.txt') as f:
    for line in f.readlines():
        text2 += line
            
#startTime = time.time()
cleanedText1 = RemoveGarbage(text1)

#f = open('test.txt','w')
#f.write(cleanedText1) # python will convert \n to os.linesep
#f.close()
#print("Time - ", time.time() - startTime)
print("Text1 after cleaning has", WordCount(cleanedText1), " words")

cleanedText2 = RemoveGarbage(text2)
print("Text2 after cleaning has", WordCount(cleanedText2), " words")

print("Unique words count in text1", UniqueWordsCount(cleanedText1))
print("Unique words count in text2", UniqueWordsCount(cleanedText2))

print("Words count in tex1 which are not in text2", UniqueNotInCount(cleanedText1, cleanedText2))

print("Unique words in both text", len(UniqueSame(cleanedText1, cleanedText2)))

#print(Alphabet(cleanedText1))