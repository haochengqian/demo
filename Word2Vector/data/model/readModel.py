from gensim.models import Word2Vec

model = Word2Vec.load('/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/model/word2vec_gensim')

print model.most_similar("liuzilin")
