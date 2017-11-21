import pandas as pd
import nltk,re,pprint
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Consumer_Complaints.csv') # READS THE  CSV FILE

def preprocess_complaint_narratives(df): # receives argument df. Is this dataframe?
	sentences = [] # CREATES AN EMPTY LIST FOR SENTECES. IS THIS SUPPOSED TO BE EMPTY?
	for doc in df: # FOR EVERY ANNOTATION IN THE CONSUMER COMPLAINT FIELD
		#Sentence tokenize
		sent = nltk.___________(doc) # GIVE SOMETHING TO MAKE THE TOKENS IN THE SENTENCES - > sent_tokenize()
		#word tokenize
		sent = [nltk.______(sent) for s in sent] # TURNS SENTENCES INTO WORDS -> word_tokenize()
		#Part of speech tagging
		sent = [nltk.______(sent) for s in sent] # NOT SURE ABOUT THIS SECTION -> pos_tag()
		for s in sent: # RUNS LOOP FOR ALL ITEMS IN SENT
			sentences.append(s) # APPENDS ALL THE ITEMS INTO SENTENCES

	return sentences

file = "notNull.csv" # my file cleaned from the null narratives
df = pd.read_csv(file)
compNarr = df['_______'] # Consumer narrative
banks = set(df['______']) # Company

tokens = preprocess_complaint_narratives(________) # compNarr
tree = [nltk.chunk.ne_chunk(t) for t in tokens]

# I NEED TO RUN THE CODE UP TO THIS POINT TO SEE WHAT KIND OF LABELS I CAN HAVE HERE
# I NEED TO SEE THE ELEMENTS OF THE TREE
def extract_entity_names(t): # A ELEMENT OF THE TREE IS SENT TO THIS FUNCTION
    entity_names = [] # CREATES AN EMPTY LIST TO STORE ENTITIES
    if hasattr(t, 'label') and t.label():
    # hasattr: The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not.
        if t.label() == '_________': # MAYBE THIS LABEL IS SUPPOSED TO BE ORGANIZATION OR SOMETHING THAT REFLECT THE ENTITY AS AN ORGANIZATION, OR MAYBE EVEN AN ELEMENT FROM A DICTIONARY, LIKE THE LIST OF BANKS
            entity_names.append(' '.join([child[0] for child in t])) # something missing # CHILD IS A LOOP COUNTER FOR ELEMENTS IN t, THIS LOOP IS TAKING THE FIRST ELEMENT IN THE LOOP
        else: # THIS IS A RECURSIVE IF!!! IF THE PREVIOUS CONDITION FAILS THEN ALL THE ELEMENTS IN THE T ARE SENT TO THIS SAME FUNCTION AND APPENDED TO THE LIST
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
