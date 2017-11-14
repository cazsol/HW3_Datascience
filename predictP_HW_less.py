import pandas as pd
import nltk
import random
from nltk.corpus import stopwords
import numpy as np
from sklearn.linear_model import LogisticRegression

stop_words = set(stopwords.words('english'))

#Remove other words from data set which are generic to all product labels
other_stop_words = {_________}
stop_words = stop_words.union(other_stop_words)

feature_words = set()

'''
Generates feature vectors for each input x, in an array of shape (len(feature_words),1) - here (63,1)
'''
def issue_features(doc):
	global feature_words
	features = {}
	words = []
	feat = np.zeros(_________)
	for s in doc.______.split():
		words.append(s)

	for word in set(words):
		if(word in feature_words):
			feat[feature_words.index(word)] = 1
	return feat

'''
Generates product labels for each output label y, in an array of shape (len(labels),1)
labels holds a list of unique output labels we have. For instance,the Product category,has 18 unique products that have been
identified from the data set. It encodes the label by setting an array with 18 - zeros and then setting the index at which the label
ccursin the original labels list to 1.
So if 'Credit Reporting' is the first label in labels list, then its y vector would be as follows:
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
'''
def product_label(p):
	global labels
	pf = np.zeros(________)
	pf[labels.index(p)] = 1
	return pf

'''
Before this step,creating the dataset by downloading it from the given site and cleaning it is upto you.
Make sure you drop NaN values before begin coding the below part.(You can use another script to clean the data and create a new .csv file to use for futher manipulation.)
'''
file = _______
df = pd.read_csv(____)
x = df['Consumer complaint narrative']
y = df[______]

#Get all the unique product labels
labels = list(df.Product._______())

top = {}
print("Getting feature list")
for label in labels:
	temp = df[df['Product']==label]['Consumer complaint narrative']
	wordc = {}
	filtered = []
	for doc in temp:
		for s in doc._______.split():
			#Use s only if s is not a stop word
			if(s not in ______):
				filtered.append(s)
				if(s in wordc):
					wordc[s] +=1
				else:
					wordc[s] = 1
	topwords = sorted(wordc.items(),key = lambda x:x[1],reverse=_____)

	#Get only the top X words for each label
	top[label] = topwords[0:____]

occ = {}
for key,val in top.items():
	for w in val:
		if(w[0] in occ):
			occ[w[0]] += w[1]
		else:
			occ[w[0]] = w[1]
		feature_words.add(w[0])

#Feature words are the top X occurring words in each label category. We consider all the unique words in this set.
feature_words = list(feature_words)

print("Number of features = " + str(len(feature_words)))
print("##########################")
print("Building feature set")

#Feature set for logistic regression
feature_set = [(issue_features(x1),y1) for x1,y1 in zip(x,y)]

#Split data into training and test data. Use 10% of the data as test data
size = int(len(feature_set)*______)

print("Feature set Generated")
print("##########################")
train_set,test_set = feature_set[_____],feature_set[_______]
trainx,trainy = zip(*train_set)
testx,testy = zip(*test_set)

#Using multi-class Logistic regression, try using other classifiers
clf = LogisticRegression(multi_class ='______',solver='lbfgs')

print("Starting the training")

clf.fit(_____,______)

print("Training completed")
print("##########################")

#To calculate accuracy
correct = 0

for x1,y1 in zip(testx,testy):
	predy = clf.predict(np.array([x1]))

	#Use below for Logistic Regression, SVM , BernoulliNB
	if(predy == ____):
		correct +=__

#Print accuracy of the model
print("Accuracy = " , _______)

'''
Above code predicts only the product given a consumer complaint narrative.
Repeat the above procedure to predict sub-product, issue and sub-issue.
Record and report the accuracy of your model's predictions.

'''
