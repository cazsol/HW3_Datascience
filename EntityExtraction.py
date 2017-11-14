import pandas as pd
import nltk,re,pprint
import matplotlib.pyplot as plt

def preprocess_complaint_narratives(df): # receives argument df. Is this dataframe?
	sentences = [] # create sentences
	for doc in df: # for every observation in the dataframe
		#Sentence tokenize
		sent = nltk.___________(doc) # give method
		#word tokenize
		sent = [nltk.______(sent) for s in sent] # give method method and input HATE ONE LINERS
		#Part of speech tagging
		sent = [nltk.______(sent) for s in sent] # give method and input | sent or doc
		for s in sent:
			sentences.append(s)

	return sentences

file = "notNull.csv" # my file cleaned from the null narratives
df = pd.read_csv(file)
compNarr = df['_______'] # Consumer narrative 
banks = set(df['______']) # Company

tokens = preprocess_complaint_narratives(________) # compNarr
tree = [nltk.chunk.ne_chunk(t) for t in tokens]

def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label():
        if t.label() == '_________':
            entity_names.append(' '.join([child[0] for child in t])) # something missing
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
	return entity_names

entity_names = [] # list as container

for t in tree:
    entity_names.extend(extract_entity_names(t)) # looks like somekind of append + the new entity just mined

# Get unique entity names
counts={} # creates a dictionary, should I put something here?
for i in entity_names:
	if(i in counts):
		counts[i] +=1
	else:
		counts[i] = 1
sort_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True) # reverse order
plt.bar(range(len(counts)), _________, align='center') # find the upper value to graph
plt.xticks(range(len(counts)), ________) # find the upper value to graph
plt.show() # displays the graph
