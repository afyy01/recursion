#factorial of a number

def factorial(n):
    
    #base case: where n=0 or n=1
    if n==0 or n==1:
        return 1
    else:
        #recursive case where we call the same factorial function again and again
        return n * factorial(n-1)


number = int(input("Which factorial would you like to know?"))
print(f"the factorial of (number) is {factorial(number)}")
#Best Case: when n==0 or n==1
#recursive case: when n>1 then it has to recursively call the same function again and again

#time complixity: 0(n) - as the number increases time also increases
#space complexity: 0(n) as number increases space / memory increases
#graph: linear 
