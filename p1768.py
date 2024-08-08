def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    w1len = len(word1)
    w2len = len(word2)
    final = []
    
    i = 0
    j = 0
    
    while i < w1len or j < w2len:
        if i < w1len:
            final.append(word1[i])
            i += 1
        if j < w2len:
            final.append(word2[j])
            j += 1
    return "".join(final)
            
word1 = "abc"
word2 = "pqr"

print(mergeAlternately(word1, word2))


        
        