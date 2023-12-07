def getHitProbability():
    # Write your code here

    R = 2
    C = 3
    #G = [(0,0,1),(1,0,1)]
    
    G = [(1,1),(1,1)]
    
    out_put = 0.0
    one_count = 0
    zero_count = 0
    
    for i in G:
        print(i)
        for j in i:
            #total_matrix_elements = len(i)
            print(j)
            if(j==1):
                one_count += 1
            elif(j==0):
                zero_count += 1

    #print(one_count)
    #print(len(G))
    out_put = one_count / (zero_count + one_count)
    print(out_put)

    return out_put


getHitProbability()  
