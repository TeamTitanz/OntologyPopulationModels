from gensim.models.keyedvectors import KeyedVectors
from collections import Counter
import glob

file_log = open("log.txt","a") 
class_file = open("files/classes","r") 
instance_file = open("files/instances","r") 
array = []
listOfArrays = [] 
word_list =[]


model = KeyedVectors.load_word2vec_format('../text8-vector.bin', binary=True)
file_log.write("Word2Vec Model loaded\n") 
print "Word2Vec Model loaded"

for line in class_file:
	if line.rstrip() == '$$$':
		listOfArrays.append(array)
		array = []

	else: 
        	array.append(line.rstrip())	
	
for instance in instance_file:
	for arr in listOfArrays:
		word = ''
		for i, item in enumerate(arr):
			if i != 0:
				word = word +" "+ item
		file_log.write("Build the word list " + word + "\n") 
		word_v = model.doesnt_match((word + " " + instance).split())
		file_log.write("Unmatch word " + word_v + " out of " + word + "\n") 
		print word_v
		if Counter(word_v.rstrip()) != Counter(instance.rstrip()):
			arr.append(instance.rstrip())
        
for arr1 in listOfArrays:
	FI = open(arr1[0], 'w')
	for i, item2 in enumerate(arr1):
  		FI.write(item2+"\n")
