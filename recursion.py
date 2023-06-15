def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])     
print(sum([5,7,3,8,10])) 

# def fibo(n):
#   if n==0:
#     return 0
#   elif n==1:
#     return 1
#   return (fibo(n-1))+(fibo(n-2)) 
# n=int(input("enter the number"))
# for i in range(n):
#   print(fibo(i))       

def re(k):
  if (k>0):
    result=k+re(k-1)
    print(result)
  else:
    result=0
  return result 
re(6) 