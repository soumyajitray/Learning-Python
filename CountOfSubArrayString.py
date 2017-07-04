class count(object):
    def wordcountinstring(self, array):

        count={}

        for i in range(len(array)):
            words=array[i].split('w')
            for j in range(len(words)):

                if words[j] not in count:
                    count[words[j]]=0
                count[words[j]]+=1


obj=count()
obj.wordcountinstring(["word1word2word3","word2word3word4","word1word2word5","word9word8word1","word7word6word4"])

# for word in array:
#     words = word.split("w")       #ranged for loop or for each loop
#     for subword in words: