def maximum(num1, num2, num3):
    if(num1<num2):
        if(num1>num2):
            return num1
        else:
            return num3 
        if(num3<num1):
            return num3
        else:
            return num1
        
Num_Vals = maximum(3,5,1)
print("Your Overall outcum is" + str(Num_Vals))

 