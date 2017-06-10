from gensim.models.keyedvectors import KeyedVectors

modified_classes = open("files/modified_classes","w") 
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
		file_log.write("Unmatch word " + word_v + "out of " + word + "\n") 
		print word_v
		if word_v != instance:
			arr.append(instance.rstrip())
		for i, item1 in enumerate(arr):
			modified_classes.write(item1+"\n")
		modified_classes.write("$$$\n")
