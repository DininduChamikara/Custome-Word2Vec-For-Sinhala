import gensim
import numpy as np

model = gensim.models.Word2Vec.load('testmodel')

# print(model.wv.most_similar("ලංකා"))
# vector = model.wv["ලංකා"]
# print(vector)

word_vector = model.wv["ඉන්දීය"]
single_value = np.mean(word_vector)  # You can also use np.sum() or other aggregation methods
print(single_value)

