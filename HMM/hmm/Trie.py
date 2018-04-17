class HZ(object):
    def __init__(self, hanzi=u"", freq=0):
        self.hanzi = hanzi
        self.freq = freq
    def __cmp__(self, other):
        return cmp(self.freq, other.freq)

class Node(object):
    def __init__(self):
        self.v = {}
        self.child = {}

class PinyinTrie(object):
    def __init__(self):
        self.root = Node()

    def add(self, pyin, hanzi):
        cur_node = self.root
        for ch in pyin:
            if ch not in cur_node.child:
                child = Node()
                cur_node.child[ch] = child
                cur_node = child
            else:
                cur_node = child
        if hanzi not in cur_node.v:
            cur_node.v[hanzi] = 1
        else:
            cur_node.v[hanzi] += 1

    def search(self, pyin):
        cur_node = self.root
        for ch in pyin:
            if ch not in cur_node.child:
                return None
            else:
                cur_node = cur_node.child[ch]
        return cur_node.v

    def des_all(self, node, hzlist):
        if node.v:
            for key in node.v:
                if key in hzlist:
                    hzlist[key] += node.v[key]
                else:
                    hzlist[key] = node.v[key]
        for ch in node.child:
            self.des_all(node.child[ch], hzlist)

    def dfs_display(self, node, py):
        if node.v:
            print(node.v)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in node.child:
                self.dfs_display(node.child[ch], py+ch)
        return

    def display_trie(self):
        self.dfs_display(self.root, "")

    def get_totalwords_of_prefix(self, node, prefix, hzlist):
        if len(prefix) == 0:
            return self.dfs_all(node, hzlist)
        if prefix[0] in node.child:
            return  self.get_totalwords_of_prefix(node.child[prefix[0]], prefix[1:], hzlist)

if __name__ == '__main__':
    trie = PinyinTrie()
    trie.add('ni', u"你")
    trie.add('ta', u"他")
    trie.add('ma', u"妈")
    trie.display_trie()

    print trie
    print trie.search('ta')
    print trie.search('made')
