from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N, D, K):
  # Write your code here
  # Traverse list D
  # Add a new variable to for completed dishes
  # intial value is 0
  # increament the value by 1 and store in a new list
  # check increment every time with k sequence and check the previous k is present in the new list. if present dont increament
  
  completed_dishes = 0
  completed_dish_list = []
  
  for i in range(1,len(D)+1):
    if (len(completed_dish_list) == 0):
      completed_dishes = completed_dishes + 1
      completed_dish_list.append(D[i])
      print(i)
      print(completed_dish_list)
    else:
        print("hi")
        for j in range(1,K+1):
            print(j)
            for l in range(j,len(completed_dish_list)+1):
                if (D[i] not in completed_dish_list):
                    completed_dishes = completed_dishes + 1
                    completed_dish_list.append(int(D[i]))
                    print(int(completed_dish_list[l]))
  
  #return 0

getMaximumEatenDishCount(6, [1,2,3,3,2,1],1)