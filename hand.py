# # # file= open("examp.txt","r")
# # # see=file.read()
# # # print("New File have value:",see)
# # # file.close()
# # # import os
# # # if os.path.exists("examp.tx"):
# # #   file.remove("examp.txt")
# # file=open("new2.txt","w")
# # c= "This is new line and new file"
# # b=file.write(c)
# # d=str(b)
# # print("New file & new line:",d)
# # file.close()
# # #
# # # # with open("examp.txt") as f:
# # # #   i= f.read()
# # # #   print(i)
# # # # with open("examp.txt","a") as f:
# # # #     f.write("I am Awais ")
# # # # # with open("examp.txt") as f:
# # # # #     print(f.read())
# # # #
# # # # with open("examp.txt", "a+") as f:
# # # #     f.write("Now the file has more content!\n")  # Add newline for clarity
# # # #     f.seek(0)  # Move cursor to beginning for reading
# # # #
# # # #     for i, line in enumerate(f):
# # # #         if i >= 2:
# # # #             break
# # # #         print(line)
# # # #
# # # #     print(line)
# # #
# # #
# # # # #open and read the file after the appending:
# # # # with open("examp.txt") as f:
# # # #   print(f.read())
# # #
# # #
# # #
# # #
# #
# # from logging import*
# # sow="{lineno}# {name}= {asctime}: {message}"
# # basicConfig(filename="logfile.log",level=NOTSET,filemode="w",style="{",format=sow)
# # debug("Debug")
# # warning("This is your warning")
# # info("Info")
# # error("Next is error")
# # critical("Critical")
# import logging
# logging.basicConfig(filename="looog.log",level="NOTSET",style="{",format="{asctime}:{name} : {message}")
# logging.debug("shoe debug")
# logging.info("show info")
# logging.warning("show warning")
# logging.error("show error")
# logging.critical("show critical")


def dec(add):
    print("Adding something")

    def inp():
        n=add()
        result=float(input("Enter 3rd Number:"))
        result=result+n
        print("Final Result is: ",result)
        inp()
    return inp
@dec
def add():
    a=float(input("Enter 1st Number:"))
    b=float(input("Enter 2nd Number:"))
    c=a+b
    return c
add()