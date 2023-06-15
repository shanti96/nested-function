"""def outer(a,b):
    num= a+b
    def inner(a,b):
        return a*b
    add=num+inner(a,b)
    return add
# result=outer(2,3)
# print(result)  
print(outer(2,3)) """

def first(a,b):
    def second(c):
        for i in range(a,b+1):
            if i%2==0:
                print("even number=",i) 
        return c+i
    n=int(input("take a number "))               
    print(second(n))
first(2,9)        