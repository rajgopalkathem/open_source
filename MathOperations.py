class Math_Operations:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        print("Two numbers are= ", self.first_num, self.second_num)
        
    def add(self):
        return ("Addition ",self.first_num + self.second_num)
    
    def subtraction(self):
        return("Subtraction ", self.first_num - self.second_num)

    def multiplication(self):
        return("Multiplcation ", self.first_num * self.second_num)
    
    def division(self):
        return ("Fractional division ", self.first_num / self.second_num)
    
    def int_division(self):
        return("Integer division ", self.first_num // self.second_num)
    
    def add_even(self):
        add_even = []
        if((self.first_num % 2) == 0):
            add_even.append("First Number is even which is " + str(self.first_num))            
        else:
            add_even.append("First Number is odd which is " + str(self.first_num))
            
        if ((self.second_num % 2) == 0):
            add_even.append("Second Number is even which is " + str(self.second_num))
        else:
            add_even.append("Second number is odd which is " + str(self.second_num))
                
        return add_even
    
    def multiples(self):
        first_num_multiples = []
        second_num_mulitiples = []
        
        for i in range(1,10): # find the multiples for 10 iterations
            first_num_multiples.append(self.first_num * i)
            second_num_mulitiples.append(self.second_num * i)
            
        print("Multiples are ")
        return first_num_multiples, second_num_mulitiples
    
    def factors(self):
        first_num_factors = []
        second_num_factors = []
        # find factors of a given number. example 3 factors are 1,3
        #6 factors are 1,2,3,6
        #10 factors are 1,2,5,10
        #12 factors are 1,2,3,4,6,12
        for i in range(1, self.first_num + 1):
            
            #print(i,(self.first_num % i))
            
            if ((self.first_num % i) == 0):
                #print(i)
                first_num_factors.append(int(i))
        
        for i in range(1, self.second_num + 1):
            
            #print(i,(self.first_num % i))
            
            if ((self.second_num % i) == 0):
                #print(i)
                second_num_factors.append(int(i))
        
        print("Factors are ")
        return first_num_factors, second_num_factors

    def factorial(self):
        #2 factorial is 2
        #3 factorial is 6
        #4 factorial is 24
        #5 factorial is 120
        
        k,l = 1,1
        for i in range(1, self.first_num):
            k = k * (i+1)
            
            #if(i < 1):
             #   return k
            #else:
             #   k = i * (i+1)
        for j in range(1, self.second_num):
            l = l * (j+1)
        
        return str(self.first_num) + " Factorial is " + str(k), str(self.second_num) + " Factorial is " + str(l)

    def fibonacci(self):
        #1,1,2,3,5,8,13,21
        
        first_num_fibonacci, second_num_fibonacci = [], []
        a,b,c = 1,1,1
        
        for k in range(1, self.first_num):
            if (k == 1):
                #c = a + b
                first_num_fibonacci.append(a) # 1
                first_num_fibonacci.append(b) # 1
                #print(a,b)
                #a = a + 1
                #b = b + 1
            else:                
                #a = c
                c = a + b #2 as a=1, b=1
                if(c < self.first_num):                    
                    a = b
                    b = c #c 3 which a = 1, b =1
                    
                    #c 5 whcih a = 2,b=3
                    
                    #print(c)
                    first_num_fibonacci.append(c)
                    
        # do the same for the second numer
        a,b,c = 1,1,1
        for l in range(1,self.second_num):
            if(l == 1):
                second_num_fibonacci.append(a)
                second_num_fibonacci.append(b)
            else:
                c = a + b
                if( c < self.second_num):                    
                    a = b
                    b = c
                    second_num_fibonacci.append(c)
                    
        return "First number fibonacci series is",first_num_fibonacci, "Second number fibonacci series is", second_num_fibonacci
        

    def LCM(self): # Leacon Common Multiplier
        first_num_multiples = []
        second_num_mulitiples = []
        
        for i in range(1,6): # find the multiples for 6 iterations
            first_num_multiples.append(self.first_num * i)
            second_num_mulitiples.append(self.second_num * i)
        
        #find a least common multiplier
        #print ("Least common multiplier")
        LCM = 0
        found = False
        for i in first_num_multiples:
            #print(i)
            #if(found == False):
            for j in second_num_mulitiples:                
                if(i==j):
                    LCM = i
                    found = True
                    break                      
                else:
                    #print (j)
                    continue
            #else:
            
        if(found == True):
            return "LCM of above both numbers is ", LCM
        else:
            return "LCM not found in 6 iterations"
        
        #print("Multiples are ")
        #return "LCM of above both numbers is ", LCM    
    def dict_example (self):            
        d1 = {"a": "apple", "b": "kiwi"}
        d2 = {"b": "strawberry", "c": "banana"}

        d1.update(d2)

        print(d1)
        return (d1["b"])

    def GCF(self):
        first_num_factors = []
        second_num_factors = []
        # find factors of a given number. example 3 factors are 1,3
        #6 factors are 1,2,3,6
        #10 factors are 1,2,5,10
        #12 factors are 1,2,3,4,6,12
        for i in range(1, self.first_num + 1):
            
            #print(i,(self.first_num % i))
            
            if ((self.first_num % i) == 0):
                #print(i)
                first_num_factors.append(int(i))
        
        for i in range(1, self.second_num + 1):
            
            #print(i,(self.first_num % i))
            
            if ((self.second_num % i) == 0):
                #print(i)
                second_num_factors.append(int(i))
        
        GCF = 0
        #found = False
        first_num_factors.reverse()
        second_num_factors.reverse()
        
        print(first_num_factors)
        print(second_num_factors)
        
        for i in first_num_factors:            
            #print(i)
            for j in second_num_factors:                
                if(i==j):
                    GCF = j
                    #found = True
                    #print(found)
                    return "GCF of above both numbers is", GCF
                    #break                      
                else:
                    #print (j)
                    continue
          
 
obj1 = Math_Operations(10,15)
print(obj1.add())
print(obj1.subtraction())
print(obj1.multiplication())
print(obj1.division())
print(obj1.int_division())
print(obj1.add_even())
print(obj1.multiples())
print(obj1.factors())
print(obj1.factorial())
print(obj1.fibonacci())
print(obj1.LCM())
print(obj1.dict_example())
print(obj1.GCF())