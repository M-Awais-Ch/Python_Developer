
def decr(intro):
    print("Hi,How are you")
    def data():
        a=int(input("Enter a 1  Number: "))
        b=int(input("Enter a 2 Number: "))
        c=intro()
        print(a+b+c)
    return data

@decr
def intro():
    c=int(input("Enter a 3  Number: "))
    return c
intro()