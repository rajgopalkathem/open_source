class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        #GGLLGG

        initial = [0,0] # (x,y)
        x = 0
        y = 0
        g = 1
        direction = "N"

        state = False
        for i in instructions:
            print i
            
            if(direction == "N"):
                #x = 0
                y = y + 1
                print (x,y)
            elif(direction == "S"):
                y = y - 1
                print (x,y)
            elif(direction == "W"):
                x = x - 1
                print (x,y)
            elif(direction == "E"):
                x = x + 1
                print (x,y)
        
            if(i == "L"):
                if(direction == "N"):
                    direction = "W"
                    #x = x - 1
                elif(direction == "W"):  
                    direction = "S"
                elif(direction == "S"):
                    direction = "E"
                elif(direction == "E"):
                    direction = "N"
                
            
        #print(x,y)
        if(x == 0 and y == 0):
            return "true"

        