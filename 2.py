"""def outer_function():
    print("outer function call")
    def inner_function():
        print("inner function call") 
    inner_function()
outer_function()      """

def out_func(frist,last):
    def in_func():
        return frist + " "+ last
    print("hello"+" "+ in_func()) 
out_func('Ram','Teja') 
    
a=[1,2,3,4]
print(a[1:])