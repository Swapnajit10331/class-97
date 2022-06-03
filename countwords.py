introString=input("enter your introduction:")
charactercount=0
wordcount=1
for i in introString:
    charactercount=charactercount+1
    if(i==""):
        wordcount=wordcount+1
print(wordcount)
print(charactercount)