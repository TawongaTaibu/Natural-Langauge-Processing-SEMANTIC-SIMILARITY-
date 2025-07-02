# Name: Tawonga Taibu
# Task Number: 12
# Task Name: Semantic Similarity

import spacy

# Load the medium language model (with word vectors).
nlp_md = spacy.load('en_core_web_md')

# Words to compare.
word1 = nlp_md("cat")
word2 = nlp_md("monkey")
word3 = nlp_md("banana")

# Display similarities using the medium model.
print("Similarity between 'cat' and 'monkey' (md):", 
      word1.similarity(word2))

print("Similarity between 'monkey' and 'banana' (md):", 
      word2.similarity(word3))

print("Similarity between 'cat' and 'banana' (md):", 
      word1.similarity(word3))

# References:
# https://spacy.io/
