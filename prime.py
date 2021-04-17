def checkprime(n):
    if(n==2 or n==3 or n==5 or n==7):
         print("prime number")
            
    elif(n%1==0 and n%n==0):
        if(n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0):
            print("prime number")
        else:
            print("not a prime")
n = int(input("enter a number:"))
checkprime(n)
