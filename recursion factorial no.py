def fac(n):
    if n==1:
        return 1
    else:
        return (n*(fac(n-1))) 
print(fac(5))  

'''def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibo(n-1)+fibo(n-2))
n=int(input("enter the number"))
for i in range(1,n+1):
    print(fibo(i)) '''          
           