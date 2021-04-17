def perfect(n):
    sum =0
    for i in range(1,n):
        if(n%i==0):
            sum=sum + i
    if(sum==n):
        print("perfect")
    else:
        print("not perfect")
def factorial(n):
        fact =1
        for i in range(1,n+1):
            fact= fact*i
        print("the factoral:",fact)    
            
def even(n):
    if(n%2==0):
        return True
    else:
        return False
n = int(input("enter a number:"))
if(even(n)):
    perfect(n)
else:
    factorial(n)
    
