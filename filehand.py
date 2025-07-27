a=[2,3,4,2,5]
with open("sample.txt","w") as f:
    a=f.write("how are you")
    print(str(a))
with open("sample.txt",'r') as f:
    print(f.read())
with open("sample.txt","a") as f:
    f.write("\nsomthing add")
with open("sample.txt",'r') as f:
    print(f.read())
