# Name: Tawonga Taibu
# Task Number: 12
# Task Name: NLP - Semantic Similarity

import spacy

# Load the simpler language model (without word vectors).
nlp_sm = spacy.load('en_core_web_sm')

# Now using the simpler language model.
word1_sm = nlp_sm("Apple")
word2_sm = nlp_sm("Wolf")
word3_sm = nlp_sm("Dog")

# Display similarities using the small model.
print("Similarity between 'Apple' and 'Wolf' (sm):", 
      word1_sm.similarity(word2_sm))

print("Similarity between 'Wolf' and 'Dog' (sm):", 
      word2_sm.similarity(word3_sm))

print("Similarity between 'Apple' and 'Dog' (sm):", 
      word1_sm.similarity(word3_sm))

# References:
# https://spacy.io/
