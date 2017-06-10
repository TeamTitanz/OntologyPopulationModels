from scipy import linalg, mat, dot
from gensim.models.keyedvectors import KeyedVectors

classList = open("files/classList","w") 
file_log = open("log.txt","a") 
class_file = open("files/classes","r") 
instance_file = open("files/instances","r") 
array = {}


model = KeyedVectors.load_word2vec_format('../text8-vector.bin', binary=True)
file_log.write("Word2Vec Model loaded\n") 
print "Word2Vec Model loaded"


for line in class_file:
	classInfo = line.rstrip()
	split_list = classInfo.split("-")
	print split_list
	array[split_list[0]] = split_list[1]
	
for instance in instance_file:
	instance = instance.rstrip()
	v =  model[instance]
	min = 0
	possible_class = ''
	for i in range(0, len(array)):
		c = dot(array[i][1],v.T)/linalg.norm(array[i][1])/linalg.norm(v)
		if min > c:	
			min = c
			possible_class = array[i][0]
	classList.write(instance + "-" + possible_class)
