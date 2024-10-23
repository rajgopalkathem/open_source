
print("hello world")

class Solution:
    def runningSum(self, nums):
        print("hi")
        print(range(len(nums)))
        test_lst = []
        for i in range(len(nums)):
            #print(i, nums[i])
            if (i < len(nums)):
                print(nums[i])
                
                if(i==0):
                    result = nums[i]
                    test_lst.append(nums[i])
                else:
                    result = result +  nums[i]
                    print("result =",result)
                    test_lst.append(result)
        
        print("test_lst")    
        print(test_lst)  
        
        add_ten = lambda x: x - 10
        print(add_ten(5))  

        return test_lst

a = Solution()
a.runningSum([1,2,3,4])
