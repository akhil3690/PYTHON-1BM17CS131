def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 

    elif n==1: 
        return 0
   
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)




print("enter the number:");
num=(int)(input("Enter the Number"))
i=0
while i< num:
         print(Fibonacci(num)) 
         i=i+1    
