class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #word1_len = len(word1)
        #word2_len = len(word2)

        #word1= "abc"
        #word2= "pqr"
        merge_string = ""
        if(len(word1) == len(word2)):
            for i in range(len(word1)):
                merge_string = merge_string + (str(word1[i])) + (str(word2[i])) 
                #print (str(word1[i]))
                #print (str(word2[i]))
                #print(merge_string)
                # + str(word2(i))
        elif(len(word1) > len(word2)):
            for i in range(len(word1)):
                if (i < len(word2)):
                    merge_string = merge_string + (str(word1[i])) + (str(word2[i])) 
                else:
                    merge_string = merge_string + (str(word1[i]))
        else:
            for i in range(len(word2)):
                if (i < len(word1)):
                    merge_string = merge_string + (str(word1[i])) + (str(word2[i])) 
                else:
                    merge_string = merge_string + (str(word2[i]))
            

        #print("result =")
        print(merge_string)
        return merge_string 
        
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
