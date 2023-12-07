class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_len = len(word1)
        word2_len = len(word2)

        #word1= "abc"
        #word2= "pqr"
        
        i1,i2 = 0,0
        merge_string = []
        
        while (i1 < word1_len or i2 < word2_len):    
            if(i1 < word1_len):
                merge_string += word1[i1]
                i1 += 1                
            if(i2 < word2_len):
                merge_string += word2[i2]                
                i2 += 1
    
        
        print(merge_string)
        print("".join(merge_string))
        return "".join(merge_string) 
        
obj1 = Solution()

word1= "abc"
word2= "pqr"
       
print(obj1.mergeAlternately(word1,word2))

word1= "abc"
word2= "pq"
       
print(obj1.mergeAlternately(word1,word2))

word1= "ab"
word2= "pqr"
       
print(obj1.mergeAlternately(word1,word2))
