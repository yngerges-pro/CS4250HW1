#-------------------------------------------------------------------------
# AUTHOR: Youstina
# FILENAME: indexing.py
# SPECIFICATION: finding document term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv

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
# print("documents2:",documents2)
#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {'cats':'cat','dogs':'dog', 'loves':'love'}

# documents3 = []

for i in range(len(steeming)):
  key = list(steeming.keys())
  value = list(steeming.values())

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

# from collections import Counter

# freq_Dic = {}
# tf = {}


# sums = {}
# for idx, d in enumerate(documents3):
#     word_counts = Counter(d) #counts words of each row (or document)
#     freq_tuple = tuple(word_counts.get(w, 0) for w in terms) #creates freq_tuple
#     freq_Dic[idx] = freq_tuple #addes freq_tuple for each set of rows or documents
#     sum_value = sum(freq_tuple)
#     sums[idx] = sum_value

# for idx, freq_tuple in freq_Dic.items():
#     print(f"Document {idx}:")
#     totalInDoc = sums[idx]
#     for term, frequency in zip(terms, freq_tuple):
#         print(f"{term}: {frequency}")
#         print("sums[idx]", sums[idx])
#         if totalInDoc != 0:
#           tf[term] = frequency/totalInDoc
#         else:
#            tf[term] = 0.0
#         print(f"TF({term}): {tf[term]}") 
#     print()

# print(freq_Dic)
# print(tf)



#Printing the document-term matrix.
#--> add your Python code here