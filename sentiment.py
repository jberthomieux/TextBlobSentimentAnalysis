
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger

text = open("hw3.txt")
filepath ="<YourPath>"
with open(filepath,'r') as mastertext:
    content=mastertext.readlines()
#print(content)

for i in range(0,len(content)):
    content[i]=content[i].replace('\t\n','')

for i in range(0,len(content)):
    t=TextBlob(content[i])
    if (t.polarity<0):
        print("Sentence",i+1,"is negative  ",end =" ")
        print(t.sentiment)
    elif(t.polarity>0):
        print("Sentence",i+1,"is positive  ",end =" ")
        print(t.sentiment)
    else:
        print("Sentence",i+1,"is neutral  ",end =" ")
        print(t.sentiment)





