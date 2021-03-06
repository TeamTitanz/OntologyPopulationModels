import numpy 
from gensim.models.keyedvectors import KeyedVectors
import glob
import os
import cPickle

file_log = open("log.txt","a") 
instance_file = open("files/instances","r") 
array = {}


model = KeyedVectors.load_word2vec_format('../text8-vector.bin', binary=True)
file_log.write("Word2Vec Model loaded\n") 
print "Word2Vec Model loaded"

with open('files/classes', 'rb') as fp:
  array_1 = cPickle.load(fp)
	
for instance in instance_file:
	instance = instance.rstrip()
	try:
		v =  model[instance]
		min = -1
		possible_class = ''
		for i in range(0, len(array_1)-1):
			c = (numpy.dot(array_1[i], v))/(numpy.linalg.norm(array_1[i])*numpy.linalg.norm(v))
			if min <= c:	
				min = c
				possible_class = array_1[-1][i]
		relevant_class = open(possible_class,"a") 
		relevant_class.write(instance+"\n")

	except KeyError:
		print instance +" is not in vocabulary"
