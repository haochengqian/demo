import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gensim.models import Word2Vec

class TextLoader(object):
    def __init__(self):
        pass

    def __iter__(self):
        input = open('mycorpus.txt','r')
        line = str(input.readline())
        counter = 0
        while line!=None and len(line) > 4:
            segments = line.split(' ')
            yield  segments
            line = str(input.readline())

sentences = TextLoader()
model = Word2Vec(sentences, workers=8)
model.save('word2vector2.model')
print 'ok'