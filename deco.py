#@decorator

def dec(add):
    print("Adding something")

    def inp():
        n=add()
        result=float(input("Enter 3rd Number:"))
        result=result+n
        print("Final Result is: ",result)
    return inp
@dec
def add():
    a=float(input("Enter 1st Number:"))
    b=float(input("Enter 2nd Number:"))
    c=a+b
    return c
add()
