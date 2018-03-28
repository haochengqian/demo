from gensim.models import Word2Vec
import pickle

f = open('vocabulary','r')

word = open('word.pkl','wb')
vector = open('vector.pkl','wb')

vocabulary = []

for row in f:
    p = row.split(' ')
    vocabulary.append(p[0])

model = Word2Vec.load('/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/model/word2vec_gensim')

for wo in vocabulary:
    pickle.dump(wo,word)
    pickle.dump(model[wo],vector)