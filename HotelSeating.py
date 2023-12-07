from typing import List
# Write any import statements here

def check_near_by(S, K, j, people_count):
    print("k,j" + str(K), str(j))
    if ((j+K) in S):
        print("not count")
        people_count =  people_count - 1
        return people_count
    else:
        people_count =  people_count + 1
        return people_count

def getMaxAdditionalDinersCount(N, K, M, S):
    # Write your code here
    #N = 10 #total seats
    #K = 1 # leave 1 seat and then sit
    #M = 2 # 2 people already sitting in the row
    #S = [2, 6] #2nd and 6th person sitting
    #capacity_available = [4, 8, 10]
    #go through the loop and add the people by skipping who are already present 

    S.sort()
    print("N, K, M are " + str(N),str(K), str(M))#N = 15
    #K = 2
    #M = 3

    
    total_capacity = [] #1 to N - total seats available in the row table
    people_count = 0 #find the remaining people
    #for i in range(1,N+1):
     #   total_capacity.append(i)
    
    #print(total_capacity)
    #print(S)
    
    for j in range((K+1),N+1,K+1): #K is the distance between the chair or empty chairs
        total_capacity.append(j)
        print(total_capacity)
        print("j=" + str(j))
        if(j not in S):
            print("j inside =" + str(j))
            people_count += 1
            print("check another value j-1 = "+str((j-1)))
            if((j+K) in S or (j-1) in S):
                print("j+k insisde inside =" + str(j+K))
                people_count -= 1
                
            #r = check_near_by(S,K, j, people_count)
            #people_count = people_count - r
            print("people count = " + str(people_count))
            
        
        
    print("people count = " + str(people_count))
    
    
    return 0

getMaxAdditionalDinersCount(10,1,2,[2,6])
#getMaxAdditionalDinersCount(15,2,3,[11,6,14])
#N = 15
#K = 2
#M = 3
#S = [11, 6, 14]
