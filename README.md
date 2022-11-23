# Medication-Suggestion
MySymptom: Medication Dictionary

This is a model that can be used to predict medication based off symptoms given. The idea behind the model is that the user enters a symptom, and a list of suggested medications will appear. The database contains a table of symptoms and a list of medications.  
1.	The data is made into the symptom-medication format.
2.	Make symptoms the target words and the associated medication the context words, and use this as the (target word, context word) pair for skipgramgeneration.
3.	After assigning labels of 1 or 0 to the pairs, feed it into the Keras model, which generates new word vectors on top of existing GloVe vectors.
4.	Loop through the set of all symptoms in the data set to find out the cosine similarity between the embeddings of the given symptom and current symptom in the loop, and then print out the symptoms with a high similarity score.
Basic cleaning, extract data from website and match synonyms. 
Cumulative list of all symptoms was made.
The Goal I want to create an extension of this project that will use the symptoms to predict the medication the person would need to help them with their symptoms. This is to help patients with their symptoms until they’re able to see their physician.
