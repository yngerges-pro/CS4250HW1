#-------------------------------------------------------------------------
# AUTHOR: Youstina
# FILENAME: indexing.py
# SPECIFICATION: finding document term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: 10 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
from collections import Counter

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append(row[0])

for i in range(len(documents)):
  documents[i] = documents[i].lower() #changes the pharases to lower cases
  
#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'i', 'she', 'her', 'and','they', 'their'}

documents2 = [] #contains list of documents without words from stopWords
for i in range(len(documents)):
  documents[i] = documents[i].split(' ')
  documents1 = list(filter(lambda item: item not in stopWords, documents[i]))
  documents2.append(documents1)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {'cats':'cat','dogs':'dog', 'loves':'love'}

#Replaces the key steeming word with value steeming word by looping through documents2
documents3 = [
    [steeming.get(word, word) for word in sub] for sub in documents2
]

print("documents3:",documents3)


#Identifying the index terms.
#--> add your Python code here
terms = []

for l in range(len(documents3)):
   for m in range(len(documents3[l])):
      if documents3[l][m] not in terms:
         terms.append(documents3[l][m])

print("Terms: ",terms)
#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []



         
freq_Dic = {}
SumPerDoc = []
freq = {}
for lit in range(len(documents3)):
  var = documents3[lit]
  row = Counter(var) #counts frequency of each doc or row
  
  freq_tuple = tuple(row.get(w, 0) for w in terms)
  freq[lit] = freq_tuple

  freq_Dic[lit] = row.values()
  SumPerDoc.append(sum(row.values()))



print(SumPerDoc)
print(freq)

TermLen = len(terms)
s = len(terms)

NumMatrix = []
for lit in freq.values():
  for index in lit:
    NumMatrix.append(index/SumPerDoc[TermLen-s])
  s -= 1


#Printing the document-term matrix.
#--> add your Python code here

docTermMatrix = NumMatrix

print(docTermMatrix)